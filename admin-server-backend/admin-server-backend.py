from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
