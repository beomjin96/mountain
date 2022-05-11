from flask import Flask, request, render_template, jsonify, url_for, redirect
from pymongo import MongoClient
import jwt, json
import datetime
import hashlib

client = MongoClient('mongodb+srv://test:sparta@cluster0.ojjgb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.mountain
app = Flask(__name__)

# JWT Encode/Decode Key
SECRET_KEY = 'MOUNTAIN'


@app.route('/mountain/add')
def add():
    return render_template('/mountain/add.html')


@app.route('/')
def home():
    return redirect(url_for('add'))


# [로그인 API]
@app.route('/mountain/login', methods=['POST'])
def api_login():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    # PASSWORD SHA256으로 암호화
    password_hash = hashlib.sha256(password_receive.encode('UTF-8')).digest()

    db.users.insert_one({'email': email_receive, 'password': password_receive})

    # 암호화 된 PASSWORD 로 DB 에서 유저 검색
    user = db.users.find_one({'email': email_receive, 'password': password_hash})

    if user is None:
        return jsonify({'result': 'fail', 'message': '아이디/비밀번호가 일치하지 않습니다.'})

    # 의문점) 이미 JWT 토큰이 있어도 다시 발급을 해줘야 하나?
    # -- 토큰이 이미 있다면 이 곳으로 올 일이 없어서 상관 없다.

    # 토큰 발급
    payload = {
        'email': email_receive,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({'result': 'success', 'token': token})


@app.route('/mountain/add', methods=['POST'])
def api_add():
    title = request.form['title']
    img_url = request.form['img_url']
    name = request.form['name']
    address = request.form['address']
    level = request.form['level']
    content = request.form['content']

    no = len(list(db.mountains.find({}))) + 1
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
            'img_url': img_url,  # sparta
            'reg_date': datetime.datetime.utcnow(),
            'name': name,
            'address': address,
            'level': level,  # number type
            'content': content
        }
        print(f"mountain = {mountain}")
        db.mountains.insert_one(mountain)

        # Check
        mountain_list = list(db.mountains.find({}))
        for mountain in mountain_list:
            print(f"mountain = {mountain}")

        response = {
            'status': 'success',
            'message': '저장을 완료했습니다.'
        }
        return jsonify(response)

    except jwt.ExpiredSignatureError:
        print(f"ExpiredSignatureError !!!")
        return redirect(url_for('home', message='로그인 시간이 만료되었습니다.'))

    except jwt.exceptions.DecodeError:
        print(f"exceptions.DecodeError !!!")
        return redirect(url_for('home', message='로그인 정보가 존재하지 않습니다.'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)