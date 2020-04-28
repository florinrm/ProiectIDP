from flask import Flask, render_template, send_from_directory
from prometheus_flask_exporter import PrometheusMetrics
import random
import os

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'db'
}

@app.route('/showItems')
def show_items():
    print("plm")


if __name__ == "__main__":
    app.run(host="0.0.0.0")

