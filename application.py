from flask import Flask, render_template, request, redirect
from icbm_code.calculations import time_horizon as th

user_score_th = th.TimeHorizon()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    # return redirect('/start')


@app.route("/start")
def start():
    # return redirect('/time-horizon')
    return render_template("time-horizon.html")


@app.route("/time-horizon", methods=["get"])
def time_horizon():
    answer = request.args.get("time_horizon")
    if not answer:
        return render_template("error.html")
    user_score_th.set_time(answer)
    print(user_score_th.get_time())
    return render_template("answers.html", answer=request.args.get("time_horizon"))

