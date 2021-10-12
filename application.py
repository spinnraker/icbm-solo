from flask import Flask, render_template, request, redirect
from icbm_code.calculations import time_horizon as th, investment_objective as io

user_score_th = th.TimeHorizon()
user_score_io = io.InvestmentObjective()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    # return redirect('/start')


@app.route("/start")
def start():
    # return redirect('/time-horizon')
    return render_template("time-horizon.html")


@app.route("/time-horizon")
def time_horizon():
    answer = request.args.get("time_horizon")
    user_score_th.set_time(answer)
    print(user_score_th.get_time())
    return render_template('/io-first.html')
    # return render_template("answers.html", answer=request.args.get("time_horizon"))

@app.route("/io-first")
def io_first():
    f_answer = request.args.get("io-first")
    user_score_io.calc_first_answer(f_answer)
    # return render_template("answers.html", f_answer=request.args.get('io-first'))
    return render_template("/io-second.html")

@app.route("/io-second")
def io_second():
    s_answer = request.args.get("io-second")
    user_score_io.calc_second_answer(s_answer)
    user_score_io.set_objective()
    print(user_score_io.get_objective())
    return render_template('answers.html', s_answer=request.args.get('io-second'))

