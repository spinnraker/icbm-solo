from icbm_code.calculations import time_risk_mix_calc as mx, \
    esg_inv_objective_etf_calc as etf

# Instantiate classes
user_score_th = mx.TimeRiskMixCalculator()
user_score_io = etf.ESGInvestmentObjectiveETFCalculator()
user_score_rp = mx.TimeRiskMixCalculator()
user_score_esg = etf.ESGInvestmentObjectiveETFCalculator()
final_mix = mx.TimeRiskMixCalculator()
final_etf = etf.ESGInvestmentObjectiveETFCalculator()


final_answers = []
horizon_answer = final_answers[0]
objective_answer = final_answers[1]
risk_answer = final_answers[2]
esg_answer = final_answers[3]
final_mix.calculate_mix(horizon_answer, risk_answer)
final_etf.select_etfs(esg_answer, objective_answer)
asset_mix = final_mix.get_mix()
# print(asset_mix)  # Not needed on final version
#
# # Determine percentage mix based on Mix Category
# data = {}
# if asset_mix == "Conservative":
#     data = {'Mixes': 'Percentages', 'Large Cap': 15, 'Mid-Cap': 5,
#             'International Equity': 5, 'Fixed Income': 65,
#             'Alternatives': 5,
#             'Cash': 5}
# elif asset_mix == "Balanced":
#     data = {'Mixes': 'Percentages', 'Large Cap': 35, 'Mid-Cap': 10,
#             'International Equity': 10, 'Fixed Income': 35,
#             'Alternatives': 5,
#             'Cash': 5}
# elif asset_mix == "Aggressive":
#     data = {'Mixes': 'Percentages', 'Large Cap': 50, 'Mid-Cap': 20,
#             'International Equity': 20, 'Fixed Income': 0,
#             'Alternatives': 5,
#             'Cash': 5}
#
# print(data)
# etf_style = final_etf.get_etf_style()
# etf_type = final_etf.get_etf_type()
# print(etf_type)
# print(etf_style)
#
# # Dynamically gets the value from the DB
# db = cluster["ICBM"]
# collection = db["ETF"]
# etfs = collection.find({"type": etf_type, "style": etf_style})
# tickers = []  # List that will hold the ticker symbols
# names = []  # List that will hold the names
# issuers = []
# categories = []
# for result in etfs:
#     tickers.append(result['symbol'])
#     names.append(result['name'])
#     issuers.append(result['issuer'])
#     categories.append(result['category'])
#
# print(names)
#
# api_data = []
# for symbol in tickers:
#     current = td.time_series(
#         symbol=symbol,
#         interval="1day",
#         outputsize=1
#     )
#     api_data.append(current.as_json())
#     list(api_data)
#     print(api_data)
#
# etf_0 = api_data[0][0]
# etf_1 = api_data[1][0]
# etf_2 = api_data[2][0]
# etf_3 = api_data[3][0]
# etf_4 = api_data[4][0]
# etf_5 = api_data[5][0]
# etf_6 = api_data[6][0]
# etf_7 = api_data[7][0]
#
# print("Final results")
# print(final_answers)
# final_answers.clear()
# print(final_answers)
#
# return render_template('answers.html', data=data, asset_mix=asset_mix,
#                        tickers=tickers, api_data=api_data, etf_0=etf_0,
#                        etf_1=etf_1, etf_2=etf_2, etf_3=etf_3, etf_4=etf_4,
#                        etf_5=etf_5, etf_6=etf_6, etf_7=etf_7, names=names,
#                        issuers=issuers, categories=categories,
#                        etf_type=etf_type,
#                        etf_style=etf_style)