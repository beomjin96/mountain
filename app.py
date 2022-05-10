import hashlib
from pymongo import MongoClient
import ssl

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
ssl._create_default_https_context = ssl._create_unverified_context

# client = MongoClient(
#     'mongodb+srv://test:sparta@cluster0.ojjgb.mongodb.net/Cluster0?retryWrites=true&w=majority')
client = MongoClient(
    'mongodb+srv://user1:user1@cluster0.ojjgb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.mountain


@app.route('/')
def home():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login_view():
    return render_template('/mountain/login.html')


@app.route('/mountain/account', methods=['GET'])
def account_view():
    return render_template('/mountain/account.html')


@app.route('/mountain/account', methods=['POST'])
def api_account():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']

    # print(
    #     f"email={email_receive}\npassword={password_receive}\nnickname={nickname_receive}")

    password_hash = hashlib.sha256(
        password_receive.encode('utf-8')).hexdigest()

    db.users.insert_one(
        {'email': email_receive, 'password': password_hash, 'nickname': nickname_receive})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
