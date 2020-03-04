from flask import Flask, render_template, send_from_directory
from redis import Redis
import random
import os

app = Flask(__name__)
app.static_folder = 'static'


'''
@app.route('/stylesheets/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename)
'''


@app.route('/')
def index():
    template = render_template('index.html')
    return template


@app.route('/page/')
def page():
    print('sex anal cu mama lui costi care e curva mare')
    template = render_template('page.html')
    return template


if __name__ == "__main__":
    app.run(host="0.0.0.0")
