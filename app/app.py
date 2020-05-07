from flask import Flask, render_template, send_from_directory
from prometheus_flask_exporter import PrometheusMetrics
import mysql.connector
import random
import os

app = Flask(__name__)
app.config["DEBUG"] = True

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'db'
}


@app.route('/', methods=["GET"])
def show_items():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

