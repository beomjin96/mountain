from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("mountain/list.html")


@app.route('/login')
def login():
    return render_template("mountain/login.html")

@app.route('/add')
def add():
    return render_template("mountain/add.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)