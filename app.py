from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
# JWT 사용을 위한 모듈 / PyJWT 패키지 설치 필요
import jwt
# 토큰 만료 시간을 위한 모듈 / datetime 패키지 설치 필요
import datetime
# PASSWORD 암호화 모듈
import hashlib

# 테스트 계정
# email: admin@naver.com
# password: admin12!

# 체크 사항
# 2. 회원가입 연동/ 담당자: 채운님
# 6. 최종 검토 및 병합/ 담당자: 상운
# 7. AWS 배포/ 담당자: 상운
client = MongoClient('mongodb+srv://test:sparta@cluster0.ojjgb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.DEV_mountain
app = Flask(__name__)

# JWT Encode/Decode Key
SECRET_KEY = 'MOUNTAIN'


# [Common Auth] ────────────────────────────────
def auth():
    token_receive = request.cookies.get('myToken')
    try:
        jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        return True

    except jwt.ExpiredSignatureError:
        print(f"로그인 시간이 만료되었습니다.")
        return False

    except jwt.exceptions.DecodeError:
        print(f"로그인 정보가 존재하지 않습니다.")
        return False


def make_star(n):
    star = ""
    for _ in range(n):
        star += "⭐"
    return star


# [Home] ────────────────────────────────
@app.route('/')
def home():
    print("Home ────────────────────────────────")
    token_receive = request.cookies.get('myToken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user = db.users.find_one({'email': payload['email']})
        return render_template('/mountain/list', email=user['email'])

    except jwt.ExpiredSignatureError:
        return redirect(url_for('view_login'))

    except jwt.exceptions.DecodeError:
        return redirect(url_for('view_login'))


# [회원가입 View] ────────────────────────────────
@app.route('/mountain/account', methods=['GET'])
def view_account():
    return render_template('/mountain/account.html')


# [회원가입 API] ────────────────────────────────
@app.route('/mountain/account', methods=['POST'])
def api_account():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']

    exists = bool(db.users.find_one({"email": email_receive, "nickname": nickname_receive}))

    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    db.users.insert_one({'email': email_receive, 'password': password_hash, 'nickname': nickname_receive})
    return jsonify({'result': 'success', 'exists': exists})


#  [회원가입 중복 이메일 닉네임 체크 API]
@app.route('/mountain/account/user', methods=["POST"])
def check_account():
    email_receive = request.form['email_give']
    nickname_receive = request.form['nickname_give']

    exists = bool(db.users.find_one({"email": email_receive}))
    exists2 = bool(db.users.find_one({"nickname": nickname_receive}))

    return jsonify({'result': 'success', 'exists': exists, 'exists2': exists2})


# [로그인 View] ────────────────────────────────
@app.route('/mountain/login')
def view_login():
    return render_template('/mountain/login.html')


# [로그인 API] ────────────────────────────────
@app.route('/mountain/login', methods=['POST'])
def api_login():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    print(f"email_receive = {email_receive}")
    print(f"password_receive = {password_receive}")

    # PASSWORD SHA256으로 암호화
    password_hash = hashlib.sha256(password_receive.encode('UTF-8')).hexdigest()

    # 암호화 된 PASSWORD 로 DB 에서 유저 검색
    user = db.users.find_one({'email': email_receive, 'password': password_hash})

    if user is None:
        return jsonify({'result': 'fail', 'message': '아이디/비밀번호가 일치하지 않습니다.'})

    # 토큰 발급
    payload = {
        'email': email_receive,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({'result': 'success', 'token': token})


# [목록 View] ────────────────────────────────
@app.route('/mountain/list')
def api_list():
    print("목록 View ────────────────────────────────")
    if auth():
        mountain_list = list(db.mountains.find({}))
        print(f"length = {len(mountain_list)}")
        for mountain in mountain_list:
            print(f"mountain = {mountain}")
            star = make_star(int(mountain['level']))
            mountain['star'] = star

        return render_template("/mountain/list.html", mountain_list=mountain_list)
    else:
        return redirect(url_for('view_login'))


# [상세보기 View] ────────────────────────────────
@app.route('/mountain/detail')
def view_detail():
    print("상세보기 View ────────────────────────────────")
    if auth():
        no_receive = int(request.args.get('no_give'))
        mountain = db.mountains.find_one({'no': no_receive})
        level = int(mountain['level'])
        star = make_star(level)
        mountain['star'] = star
        print(f"mountain = {mountain}")
        return render_template("/mountain/detail.html", mountain=mountain)
    else:
        return redirect(url_for('view_login'))


# [등록 View] ────────────────────────────────
@app.route('/mountain/add')
def view_add():
    if auth():
        return render_template('/mountain/add.html')
    else:
        return redirect(url_for('view_login'))


# [등록 API] ────────────────────────────────
@app.route('/mountain/add', methods=['POST'])
def api_add():
    print("등록 API ────────────────────────────────")
    title = request.form['title']
    name = request.form['name']
    address = request.form['address']
    level = request.form['level']
    content = request.form['content']
    print(f"title={title}\nname={name}\naddress={address}\nlevel={level}\ncontent={content}")

    # 파일 업로드
    file = request.files["file"]
    today = datetime.datetime.now()
    my_time = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{my_time}'
    extension = file.filename.split('.')[-1]
    save_to = f'static/images/mountain/{filename}.{extension}'
    file.save(save_to)
    # //파일 업로드

    sequence = 1
    for item in list(db.mountains.find({})):
        sequence = max(sequence, int(item['no']))
    no = sequence + 1
    token_receive = request.cookies.get('myToken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user = db.users.find_one({'email': payload['email']})
        print(f"user =  {user}")
        print(f"user['email'] = {user['email']}")

        mountain = {
            'no': no,
            'title': title,
            'email': user['email'],
            'image': f'{filename}.{extension}',  # 파일 업로드
            'reg_date': datetime.datetime.utcnow(),
            'name': name,
            'address': address,
            'level': int(level),
            'content': content
        }
        print(f"mountain = {mountain}")
        db.mountains.insert_one(mountain)

        # 확인
        mountain_list = list(db.mountains.find({}))
        for mountain in mountain_list:
            print(f"mountain = {mountain}")

        return jsonify({'result': 'success'})

    except jwt.ExpiredSignatureError:
        return redirect(url_for('home', message='로그인 시간이 만료되었습니다.'))

    except jwt.exceptions.DecodeError:
        return redirect(url_for('home', message='로그인 정보가 존재하지 않습니다.'))


# [삭제 API] ────────────────────────────────
@app.route('/mountain/delete', methods=['POST'])
def api_delete():
    print("삭제 API ────────────────────────────────")
    no_receive = request.form['no_give']
    db.mountains.delete_one({'no': int(no_receive)})
    print(f"no_receive = {no_receive}")
    return jsonify({'result': 'success'})


# [수정 View] ────────────────────────────────
@app.route('/mountain/update')
def view_update():
    print("수정 View ────────────────────────────────")
    if auth():
        no_receive = int(request.args.get('no'))
        print(f"no_receive = {no_receive}")
        mountain = db.mountains.find_one({'no': no_receive})
        print(f"mountain = {mountain}")
        return render_template('/mountain/update.html', mountain=mountain)
    else:
        return redirect(url_for('view_login'))


# [수정 API] ────────────────────────────────
@app.route('/mountain/update', methods=['POST'])
def api_update():
    print("수정 API ────────────────────────────────")
    no = request.form['no']
    title = request.form['title']
    image = db.mountains.find_one({'no': int(no)})['image']
    name = request.form['name']
    address = request.form['address']
    level = request.form['level']
    content = request.form['content']

    mountain = {
        'title': title,
        'image': image,
        'name': name,
        'address': address,
        'level': level,
        'content': content
    }
    print(f"mountain = {mountain}")
    db.mountains.update_one({'no': int(no)}, {'$set': mountain})
    return jsonify({"result": "success"})


if __name__ == '__main__':
    app.run()