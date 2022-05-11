import datetime

from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import timedelta, time, timezone, date
import certifi

app = Flask(__name__)
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.ojjgb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.mountain


@app.route('/')
def main():
    return redirect(url_for('home'))


@app.route('/mountain/list')
def home():
    mountain_list = list(db.mountains.find({}))
    print(f"length = {len(mountain_list)}")
    for mountain in mountain_list:
        print(f"mountain = {mountain}")
    return render_template("/mountain/list.html", mountain_list=mountain_list)


@app.route('/mountain/login')
def login():
    return render_template("mountain/login.html")


@app.route('/mountain/add')
def add():
    return render_template("mountain/add.html")


@app.route('/mountain/test/add')
def users():
    no = len(list(db.mountains.find({}))) + 1
    dummy = {
        'no': no,
        'name': '한라산',
        'title': '한라산 다녀 왔습니다!',
        'img_src': 'path',
        'nickname': '홍길동',
        'reg_datex': datetime.datetime.today(),
        'address': '제주도 제주시',
        'level': 3,
        'content': '좋은 공기 마시고 왔습니다!',
        'star_image': '⭐'.repeat('level')
    }
    print(f'dummy = {dummy}')

    db.mountains.insert_one(dummy)
    mountain_list = list(db.mountains.find({}))
    print(f"length = {len(mountain_list)}")
    for mountain in mountain_list:
        print(f"mountain = {mountain}")

    return jsonify({'message': 'success'})


@app.route('/mountain/detail_test')
def detail_test():
    mountain_list = list(db.mountains.find({}))
    print(f"length = {len(mountain_list)}")
    for item in mountain_list:
        print(f"detail = {item}")

    return jsonify({'details': mountain_list})


@app.route('/mountain/detail')
def detail():
    # no_receive = request.args.get('no_give')
    no_receive = 1
    mountain = db.mountains.find_one({'no': no_receive})
    print(f"mountain = {mountain}")

    return render_template("/mountain/detail.html", mountain=mountain)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)