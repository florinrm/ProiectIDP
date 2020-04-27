from flask import Flask, render_template, send_from_directory
import random
import os

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

