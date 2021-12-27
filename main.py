from flask import Flask, render_template, request, redirect, jsonify, url_for, \
    abort
import requests
import json
from ast import literal_eval
from icbm_code.calculations import time_risk_mix_calc as mx, \
    esg_inv_objective_etf_calc as etf
from twelvedata import TDClient
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://chrono:Pb1YS8VIIGpmRuOi@cluster0.dfgj3.mongodb.net/ICBM?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

# Twelvedata API key
td = TDClient(apikey="8f91b729c73c4b57b3ceb054ee727a2f")

# Instantiate classes
user_score_th = mx.TimeRiskMixCalculator()
user_score_io = etf.ESGInvestmentObjectiveETFCalculator()
user_score_rp = mx.TimeRiskMixCalculator()
user_score_esg = etf.ESGInvestmentObjectiveETFCalculator()
final_mix = mx.TimeRiskMixCalculator()
final_etf = etf.ESGInvestmentObjectiveETFCalculator()

final_answers = []

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(IndexError)
def index_error(e):
    return render_template('500.html')


@app.errorhandler(500)
def index_error(e):
    return render_template('500.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/start")
def start():
    return render_template("time-horizon.html")


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
    user_score_io.calc_io_first_answer(f_answer)
    return render_template("/io-second.html")



"""Name of the route will is whatever the last render_template"""
@app.route("/io-second")
def io_second():
    """create variable that will hold the user's answers"""
    s_answer = request.args.get("io-second")
    """Pass that variable to the function that calculates the score"""
    user_score_io.calc_io_second_answer(s_answer)
    """Once you reach the last question of a category, call the SET function"""
    user_score_io.set_objective()
    """After calling SET function, call the GET function"""
    print(user_score_io.get_objective())
    final_answers.append(user_score_io.get_cat())
    return render_template("/rp-first.html")


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


@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.2f}".format(value)


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
    data = {}
    mixes = {'Conservative': {'Mixes': 'Percentages', 'Large Cap': 15, 'Mid-Cap': 5,'International Equity': 5,
                              'Fixed Income': 65, 'Alternatives': 5, 'Cash': 5},
             'Balanced': {'Mixes': 'Percentages', 'Large Cap': 35, 'Mid-Cap': 10, 'International Equity': 10,
                          'Fixed Income': 35, 'Alternatives': 5, 'Cash': 5},
             'Aggressive': {'Mixes': 'Percentages', 'Large Cap': 50, 'Mid-Cap': 20, 'International Equity': 20,
                            'Fixed Income': 0, 'Alternatives': 5, 'Cash': 5}}
    data = mixes[asset_mix]
    print(data)
    etf_style = final_etf.get_etf_style()
    etf_type = final_etf.get_etf_type()
    print(etf_type)
    print(etf_style)

    # Dynamically gets the value from the DB
    db = cluster["ICBM"]
    collection = db["ETF"]
    etfs = collection.find({"type": etf_type, "style": etf_style})
    tickers = []  # List that will hold the ticker symbols
    names = []  # List that will hold the names
    issuers = []
    categories = []
    for result in etfs:
        tickers.append(result['symbol'])
        names.append(result['name'])
        issuers.append(result['issuer'])
        categories.append(result['category'])

    print(names)

    api_data = []
    for symbol in tickers:
        current = td.time_series(
            symbol=symbol,
            interval="1day",
            outputsize=1
        )
        api_data.append(current.as_json())
        list(api_data)
        print(api_data)

    etf_0 = api_data[0][0]
    etf_1 = api_data[1][0]
    etf_2 = api_data[2][0]
    etf_3 = api_data[3][0]
    etf_4 = api_data[4][0]
    etf_5 = api_data[5][0]
    etf_6 = api_data[6][0]
    etf_7 = api_data[7][0]

    print("Final results")
    print(final_answers)
    final_answers.clear()
    print(final_answers)

    return render_template('answers.html', data=data, asset_mix=asset_mix,
                           tickers=tickers, api_data=api_data, etf_0=etf_0,
                           etf_1=etf_1, etf_2=etf_2, etf_3=etf_3, etf_4=etf_4,
                           etf_5=etf_5, etf_6=etf_6, etf_7=etf_7, names=names,
                           issuers=issuers, categories=categories,
                           etf_type=etf_type,
                           etf_style=etf_style)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test")
def testing_api():
    print("Start")
    test_etf = []
    user_score_th.set_time('a')
    test_etf.append(user_score_th.get_th_cat())
    user_score_rp.calc_first_answer('a')
    user_score_rp.calc_second_answer('a')
    user_score_rp.calc_third_answer('a')
    user_score_rp.calc_fourth_answer('a')
    user_score_th.set_risk_score()
    test_etf.append(user_score_th.get_risk_cat())
    # user_score_th.calculate_mix()
    user_score_th.get_mix()
    user_score_io.calc_io_first_answer('a')
    user_score_io.calc_io_second_answer('a')
    user_score_io.set_objective()
    test_etf.append(user_score_io.get_cat())
    user_score_esg.calc_first_answer('e')
    user_score_esg.calc_second_answer('e')
    user_score_esg.calc_third_answer('e')
    user_score_esg.calc_fourth_answer('e')
    user_score_esg.set_esg_cat()
    test_etf.append(user_score_esg.get_esg_cat())
    print("Done")
    objective_answer = test_etf[2]
    esg_answer = test_etf[3]
    final_etf.select_etfs(esg_answer, objective_answer)
    asset_mix = final_mix.get_mix()

    mixes = {'Conservative': {'Mixes': 'Percentages', 'Large Cap': 15, 'Mid-Cap': 5,
                             'International Equity': 5, 'Fixed Income': 65,
                             'Alternatives': 5,
                             'Cash': 5},
            'Balanced': {'Mixes': 'Percentages', 'Large Cap': 35, 'Mid-Cap': 10,
                         'International Equity': 10, 'Fixed Income': 35,
                         'Alternatives': 5,
                         'Cash': 5},
            'Aggressive': {'Mixes': 'Percentages', 'Large Cap': 50, 'Mid-Cap': 20,
                           'International Equity': 20, 'Fixed Income': 0,
                           'Alternatives': 5,
                           'Cash': 5}}

    data = mixes[asset_mix]
    etf_style = final_etf.get_etf_style()
    etf_type = final_etf.get_etf_type()
    print(etf_type)
    print(etf_style)

    print("DB")
    db = cluster["ICBM"]
    collection = db["ETF"]
    etfs = collection.find({"type": etf_type, "style": etf_style})

    tickers = []  # List that will hold the ticker symbols
    names = []
    issuers = []
    categories = []
    for result in etfs:
        tickers.append(result['symbol'])
        names.append(result['name'])
        issuers.append(result['issuer'])
        categories.append(result['category'])
    print(tickers)

    # print("batch api calls 1")
    api_data = []
    for symbol in tickers:
        current = td.time_series(
            symbol=symbol,
            interval="1day",
            outputsize=1
        )
        api_data.append(current.as_json())
        list(api_data)

    etf_0 = api_data[0][0]
    etf_1 = api_data[1][0]
    etf_2 = api_data[2][0]
    etf_3 = api_data[3][0]
    etf_4 = api_data[4][0]
    etf_5 = api_data[5][0]
    etf_6 = api_data[6][0]
    etf_7 = api_data[7][0]

    test_etf.clear()
    print(test_etf)

    return render_template('answers.html', asset_mix=asset_mix,
                           tickers=tickers, api_data=api_data, etf_0=etf_0,
                           etf_1=etf_1, etf_2=etf_2, etf_3=etf_3, etf_4=etf_4,
                           etf_5=etf_5, etf_6=etf_6, etf_7=etf_7, names=names,
                           issuers=issuers, categories=categories,
                           etf_type=etf_type, data=data,
                           etf_style=etf_style)


#


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
