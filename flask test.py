from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Привет!</p>"


@app.route("/")
def print_time():
    return f"<p>{datetime.now()}</p>"


app.run()

