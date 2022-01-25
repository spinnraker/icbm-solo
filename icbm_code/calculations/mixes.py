import time_risk_mix_calc as mx
import esg_inv_objective_eft_calc as eft

user_score_th = mx.TimeRiskMixCalculator()
user_score_io = etf.ESGInvestmentObjectiveETFCalculator()
user_score_rp = mx.TimeRiskMixCalculator()
user_score_esg = etf.ESGInvestmentObjectiveETFCalculator()
final_mix = mx.TimeRiskMixCalculator()
final_etf = etf.ESGInvestmentObjectiveETFCalculator()


class MixCalculator:
    """Performs final calculation"""
    def __init__(self, horizon_answer='', objective_answer='', risk_answer='', esg_answer='', asset_mix=''):
        self.horizon_answer = horizon_answer
        self.objective_answer = objective_answer
        self.risk_answer = risk_answer
        self.esg_answer = esg_answer
        self.asset_mix = asset_mix

    def answers(self, final_answers=[], *args):
        self.horizon_answer = final_answers[0]
        self.objective_answer = final_answers[1]
        self.risk_answer = final_answers[2]
        self.esg_answer = final_answers[3]

    def h_answer(self):
        return self.horizon_answer

    def mixes(self):
        mixes = {'Conservative': {'Mixes': 'Percentages', 'Large Cap': 15, 'Mid-Cap': 5, 'International Equity': 5,
                                  'Fixed Income': 65, 'Alternatives': 5, 'Cash': 5},
                 'Balanced': {'Mixes': 'Percentages', 'Large Cap': 35, 'Mid-Cap': 10, 'International Equity': 10,
                              'Fixed Income': 35, 'Alternatives': 5, 'Cash': 5},
                 'Aggressive': {'Mixes': 'Percentages', 'Large Cap': 50, 'Mid-Cap': 20, 'International Equity': 20,
                                'Fixed Income': 0, 'Alternatives': 5, 'Cash': 5}}


test = MixCalculator()
h = test.h_answer()
print(h)