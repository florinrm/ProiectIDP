from flask import Flask, render_template, send_from_directory
from redis import Redis
import random
import os

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/login-check')
def login_check():
    template = render_template('index.html')
    return template

@app.route('/')
def index():
    template = render_template('index.html')
    print('plm')
    return template


@app.route('/page/')
def page():
    template = render_template('page.html')
    return template


if __name__ == "__main__":
    app.run(host="0.0.0.0")
