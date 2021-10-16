from flask import Flask, render_template, request, redirect, jsonify, url_for
from icbm_code.calculations import time_horizon as th, \
    investment_objective as io, risk_profile as rp, esg

# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.plot as plt
# import Bumpy as np

# Instantiate classes
user_score_th = th.TimeHorizon()
user_score_io = io.InvestmentObjective()
user_score_rp = rp.RiskProfile()
user_score_esg = esg.EnvironmentalSocialGovernance()

final_answers = {}

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


#
# @app.route("/answers")
# def start():
#
#     # Just need to replace these hard codes with our dynamics entries.
#     y = np.array([35, 25, 25, 15])
#
#     plt.pie(y)
#     plt.show()
#     return render_template("answers.html")

@app.route("/time-horizon")
def time_horizon():
    answer = request.args.get("time_horizon")
    user_score_th.set_time(answer)
    print(user_score_th.get_time())
    # final_answers.append(user_score_th.get_time())
    final_answers['Horizon'] = user_score_th.get_time()
    return render_template('/io-first.html')
    # return render_template("answers.html", answer=request.args.get("time_horizon"))


@app.route("/io-first")
def io_first():
    f_answer = request.args.get("io-first")
    user_score_io.calc_first_answer(f_answer)
    # return render_template("answers.html", f_answer=request.args.get('io-first'))
    return render_template("/io-second.html")


# How to create new routes or pages:

@app.route(
    "/io-second")  # Name of the route will is whatever the last render_template (right above) shows
def io_second():  # create new function, and named it the same as the route
    s_answer = request.args.get(
        "io-second")  # create variable that will hold the user's answers
    user_score_io.calc_second_answer(
        s_answer)  # Pass that variable to the function that calculates the score
    user_score_io.set_objective()  # Once you reach the last question of a category, call the SET function
    print(
        user_score_io.get_objective())  # After calling SET function, call the GET function
    # final_answers.append(user_score_io.get_objective())
    final_answers['Investment Objective'] = user_score_io.get_objective()
    return render_template(
        "/rp-first.html")  # point to the next question, then go to that HTML page file under templates and create a new form.
    # Repeat the process with as many questions as needed. Once you create all the
    # questions for a category (risk profile, esg, etc.) move to the next category


@app.route("/rp-first")
def rp_first():
    rp1_answer = request.args.get("rp-first")
    user_score_rp.calc_first_answer(rp1_answer)
    return render_template("/rp-second.html")


@app.route("/rp-second")
def rp_second():
    rp2_answer = request.args.get("rp-second")
    user_score_rp.calc_second_answer(rp2_answer)
    return render_template("/rp-third.html")


@app.route("/rp-third")
def rp_third():
    rp3_answer = request.args.get("rp-third")
    user_score_rp.calc_third_answer(rp3_answer)
    return render_template("/rp-fourth.html")


@app.route("/rp-fourth")
def rp_fourth():
    rp4_answer = request.args.get("rp-fourth")
    user_score_rp.calc_fourth_answer(rp4_answer)
    user_score_rp.set_risk_score()
    print(user_score_rp.get_risk_category())
    final_answers['Risk Tolerance'] = user_score_rp.get_risk_category()
    return render_template("/esg-first.html")


@app.route("/esg-first")
def esg_first():
    esg1_answer = request.args.get("esg-first")
    user_score_esg.calc_first_answer(esg1_answer)
    # user_score_esg.set_objective()  # SET function
    return render_template("/esg-second.html")


@app.route("/esg-second")
def esg_second():
    esg2_answer = request.args.get("esg-second")
    user_score_esg.calc_second_answer(esg2_answer)
    return render_template("/esg-third.html")


@app.route("/esg-third")
def esg_third():
    esg3_answer = request.args.get("esg-third")
    user_score_esg.calc_third_answer(esg3_answer)
    return render_template("/esg-fourth.html")


@app.route("/esg-fourth")
def esg_fourth():
    esg4_answer = request.args.get("esg-fourth")
    user_score_esg.calc_fourth_answer(esg4_answer)
    user_score_esg.set_esg_cat()
    print(user_score_esg.get_est_cat())  # GET function
    final_answers['ESG'] = user_score_esg.get_est_cat()
    return render_template("/answers.html")  # point to answers.html, since no questions remain


@app.route("/api")
def show_results():
    return jsonify(final_answers)
