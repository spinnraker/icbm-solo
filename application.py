from typing import List, Any
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_pymongo import PyMongo
from icbm_code.calculations import time_risk_mix_calc as mx, \
    investment_objective as io, risk_profile as rp, esg_inv_objective_etf_calc \
    as etf

from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://chrono:Pb1YS8VIIGpmRuOi@cluster0.dfgj3.mongodb.net/ICBM?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

# db = cluster["ICBM"]
# collection = db["ETF"]

# results = collection.find({"type": "Value", "style": "Non-ESG"})
#
# for results in results:
#     print(results["ticker"])++++++++++++++++++


# Instantiate classes
user_score_th = mx.TimeRiskMixCalculator()
user_score_io = etf.ESGInvestmentObjectiveETFCalculator()
user_score_rp = mx.TimeRiskMixCalculator()
user_score_esg = etf.ESGInvestmentObjectiveETFCalculator()
final_mix = mx.TimeRiskMixCalculator()
final_etf = etf.ESGInvestmentObjectiveETFCalculator()

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://chrono:Pb1YS8VIIGpmRuOi@cluster0.dfgj3.mongodb.net"
# mongo = PyMongo(app)

# Each question is on a separate page
@app.route('/')  # What the user sees when visiting the site
def index():
    return render_template("index.html")


@app.route("/start")
def start():
    return render_template("time-horizon.html")


final_answers: list[Any] = []

@app.route("/time-horizon")
def time_horizon():
    answer = request.args.get("time_horizon")
    user_score_th.set_time(answer)
    print(user_score_th.get_time())
    final_answers.append(user_score_th.get_th_cat())
    return render_template('/io-first.html')


@app.route("/io-first")
def io_first():
    f_answer = request.args.get("io-first")
    user_score_io.calc_first_answer(f_answer)
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
    final_answers.append(user_score_io.get_cat())
    # value = user_score_io.get_cat()
    # final_answers['Investment Objective'] = value
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
    final_answers.append(user_score_rp.get_risk_cat())
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
    print(user_score_esg.get_esg_cat())
    final_answers.append(user_score_esg.get_esg_cat())
    print(final_answers)
    return redirect("/results")


@app.route("/results")
def mix_calculator():
    horizon_answer = final_answers[0]
    objective_answer = final_answers[1]
    risk_answer = final_answers[2]
    esg_answer = final_answers[3]
    final_mix.calculate_mix(horizon_answer, risk_answer)
    final_etf.select_etfs(esg_answer, objective_answer)
    asset_mix = final_mix.get_mix()
    print(asset_mix)  # Not needed on final version


    # Determine percentage mix based on Mix Category
    # SUPER TEMPORARY FIX - want to get values from a list of dic
    if asset_mix == "Conservative":
        data = {'Mixes': 'Percentages', 'Large Cap': 15, 'Mid-Cap': 5,
                'International Equity': 5, 'Fixed Income': 65,
                'Alternatives': 5,
                'Cash': 5}
    elif asset_mix == "Balanced":
        data = {'Mixes': 'Percentages', 'Large Cap': 35, 'Mid-Cap': 10,
                'International Equity': 10, 'Fixed Income': 35,
                'Alternatives': 5,
                'Cash': 5}
    elif asset_mix == "Aggressive":
        data = {'Mixes': 'Percentages', 'Large Cap': 50, 'Mid-Cap': 20,
                'International Equity': 20, 'Fixed Income': 0,
                'Alternatives': 5,
                'Cash': 5}


    etf_style = final_etf.get_etf_style()
    etf_type = final_etf.get_etf_type()
    print(etf_type)
    print(etf_style)

    # Dynamically gets the value from the DB
    db = cluster["ICBM"]
    collection = db["ETF"]
    etfs = collection.find({"type": etf_type, "style": etf_style})
    tickers = [] # List that will hold the ticker symbols
    for result in etfs:
        tickers.append(result['ticker'])

    print(final_answers)
    return render_template('answers.html', data=data, asset_mix=asset_mix,
                           user_esg=esg_answer, user_io=objective_answer,
                           etf_style=etf_style, etf_type=etf_type,
                           results=tickers)


@app.route("/api")
def etf_cal():
    objective_answer = final_answers[1]
    esg_answer = final_answers[3]
    for_api = []

    if esg_answer == "Low":
        for_api.append("Non-ESG")
        if objective_answer == "Income":
            for_api.append("Value")
        elif objective_answer == "Balanced":
            for_api.append("Balanced")
        elif objective_answer == "Growth":
            for_api.append('Growth')
        # This portion needs to be updated once we figure out how to show both
    elif esg_answer == "Medium":
        for_api.append("ESG")
        if objective_answer == "Income":
            for_api.append("Value")
        elif objective_answer == "Balanced":
            for_api.append("Balanced")
        elif objective_answer == "Growth":
            for_api.append("Growth")
    elif esg_answer == "High":
        for_api.append("ESG")
        if objective_answer == "Income":
            for_api.append("Value")
        elif objective_answer == "Balanced":
            for_api.append("Balanced")
        elif objective_answer == "Growth":
            for_api.append("Growth")
    else:
        for_api.append("No style")
        for_api.append("No type")

    return jsonify(list(for_api))

# Not using this for now
# @app.route('/pie')
# def google_pie_chart():
#     data = {'Mixes': 'Percentages', 'Large Cap': 50, 'Mid-Cap': 20,
#                 'International Equity': 20, 'Fixed Income': 0,
#                 'Alternatives': 5,
#                 'Cash': 5}
#     return render_template('pie-chart.html', data=data)


# @app_route("/test")
# def testing_page:
#