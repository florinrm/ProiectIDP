from flask import Flask, render_template, request
import mysql.connector as connector
from redis import Redis
import random
import os

app = Flask(__name__)
app.static_folder = 'static'

config_db = {
'user': 'db',
'password': '1224',
'host': 'db',
'port': '3306',
'database': 'db'
}


def check_password(username, password):
    conn = connector.connect(**config_db)
    cursor = conn.cursor()
    passw = None
    try:
        cursor.execute("SELECT password from USERS WHERE USERNAME = %s", username)
        passw = cursor.fetchall()
    except connector.Error:
        print('error from getting password')
    finally:
        conn.commit()
        cursor.close()
        conn.close()
    if passw is None:
        return passw == password
    return None


@app.route('/login-check', methods=['GET', 'POST'])
def login_check():
    template = render_template('index.html')
    if request.method == 'POST':
        info = request.form
        user = info['username']
        password = info['password']
        print(user, password)
        result = check_password(user, password)
        if result is None:
            if result:
                return render_template("page.html")
    return template


@app.route('/', methods=['GET', 'POST'])
def index():
    template = render_template('index.html')
    return template


@app.route('/page/', methods=['GET', 'POST'])
def page():
    template = render_template('page.html')
    return template


if __name__ == "__main__":
    app.run(host="0.0.0.0")
