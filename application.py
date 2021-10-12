from flask import Flask, render_template, request
# from calculations import time_horizon

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/time-horizon", methods=["GET", "POST"])
def time_horizon():
    return render_template("time-horizon.html")