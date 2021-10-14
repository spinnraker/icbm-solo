from flask import Flask, render_template, request, redirect
from icbm_code.calculations import time_horizon as th, \
    investment_objective as io, risk_profile as rp, esg

# Instantiate classes
user_score_th = th.TimeHorizon()
user_score_io = io.InvestmentObjective()
user_score_rp = rp.RiskProfile()
user_score_esg = esg.EnvironmentalSocialGovernance()

app = Flask(__name__)

# Each question is on a separate page

@app.route('/')  # What the user sees when visiting the site
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

# How to create new routes or pages:

@app.route("/io-second") # Name of the route will is whatever the last render_template (right above) shows
def io_second(): # create new function, and named it the same as the route
    s_answer = request.args.get("io-second") # create variable that will hold the user's answers
    user_score_io.calc_second_answer(s_answer) # Pass that variable to the function that calculates the score
    user_score_io.set_objective() # Once you reach the last question of a category, call the SET function
    print(user_score_io.get_objective())    # After calling SET function, call the GET function
    return render_template("/rp-first.html") # point to the next question, then go to that HTML page file under templates and create a new form.
                                            # Repeat the process with as many questions as needed. Once you create all the
                                            # questions for a category (risk profile, esg, etc.) move to the next category

