from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
# JWT 사용을 위한 모듈 / PyJWT 패키지 설치 필요
import jwt
# 토큰 만료 시간을 위한 모듈 / datetime 패키지 설치 필요
import datetime
# PASSWORD 암호화 모듈
import hashlib

client = MongoClient('mongodb+srv://test:sparta@cluster0.ojjgb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

# JWT Encode/Decode Key
SECRET_KEY = 'MOUNTAIN'


@app.route('/')
def home():
    token_receive = request.cookies.get('myToken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user = db.users.find_one({'email': payload['email']})
        return render_template('index.html', nickname=user['nickname'])

    except jwt.ExpiredSignatureError:
        return redirect(url_for('mountain/login', message='로그인 시간이 만료되었습니다.'))

    except jwt.exceptions.DecodeError:
        return redirect(url_for('mountain/login', message='로그인 정보가 존재하지 않습니다.'))


@app.route('/mountain/login')
def login():
    return render_template('/mountain/login.html')


# [로그인 API]
@app.route('/mountain/login', methods=['POST'])
def api_login():
    email_receive = request.form['id_give']
    password_receive = request.form['password_give']

    # PASSWORD SHA256으로 암호화
    password_hash = hashlib.sha256(password_receive.encode('UTF-8')).digest()

    # 암호화 된 PASSWORD 로 DB 에서 유저 검색
    user = db.users.find_one({'email': email_receive, 'password': password_hash})
    print(f'user = {user}')

    if user is None:
        return jsonify({'result': 'fail', 'message': '아이디/비밀번호가 일치하지 않습니다.'})

    # 의문점) 이미 JWT 토큰이 있어도 다시 발급을 해줘야 하나?
    # 토큰 발급
    payload = {
        'email': email_receive,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('UTF-8')
    return jsonify({'result': 'success', 'token': token})


if __name__ == '__main__':
    app.run()