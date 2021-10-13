import time_horizon as th
import risk_profile as rp

final_th = th.TimeHorizon()
final_rp = rp.RiskProfile()

# final_th.set_time('a')

# print(final_th.horizon_category)

class MixCalculator:
    """Calculate security mix based on time horizon and risk tolerance"""

    def __init__(self, asset_mix=""):
        self.asset_mix = asset_mix

    def calculate_mix(self):
        horizon_answer = final_th.horizon_category
        risk_answer = final_rp.risk_category
        if horizon_answer == "Short Term" and risk_answer == "Conservative":
            self.asset_mix = "Conservative"
        elif horizon_answer == "Short Term" and risk_answer == "Moderate":
            self.asset_mix = "Conservative"
        elif horizon_answer == "Short Term" and risk_answer == "Aggressive":
            self.asset_mix = "Balanced"
        elif horizon_answer == "Intermediate Term" and \
                risk_answer == "Conservative":
            self.asset_mix = "Conservative"
        elif horizon_answer == "Intermediate Term" and \
                risk_answer == "Moderate":
            self.asset_mix = "Balanced"
        elif horizon_answer == "Intermediate Term" and \
                risk_answer == "Aggressive":
            self.asset_mix = "Aggressive"
        elif horizon_answer == "Long Term" and risk_answer == "Conservative":
            self.asset_mix = "Balanced"
        elif horizon_answer == "Long Term" and risk_answer == "Moderate":
            self.asset_mix = "Balanced"
        elif horizon_answer == "Long Term" and risk_answer == "Aggressive":
            self.asset_mix = "Aggressive"

        return self.asset_mix


final_th.set_time('a')
final_rp.calc_first_answer('c')
final_rp.calc_second_answer('c')
final_rp.calc_third_answer('c')
final_rp.calc_fourth_answer('c')

final_rp.set_risk_score()

my_mix = MixCalculator()

print(my_mix.calculate_mix())


