from icbm_code.calculations.time_horizon import TimeHorizon
from icbm_code.calculations.risk_profile import RiskProfile


user_th = TimeHorizon()
user_rp = RiskProfile()

user_th.set_time('a')
testing = user_th.get_time()


user_rp.calc_first_answer('a')
user_rp.calc_second_answer('a')
user_rp.calc_third_answer('a')
user_rp.calc_fourth_answer('a')
user_rp.set_risk_score()


#
#
print(user_rp.risk_category)


# testing2 = user_rp.get_risk_category()
# print(testing2)

class AssetMixes:
    """Stores the asset mixes for each risk profile"""

    def __init__(self, labels=None, sizes=None, message=''):
        """Define AssetMix class attributes"""
        if labels is None:
            labels = []
        self.labels = labels
        self.sizes = sizes
        self.message = message

    def set_labels(self):
        self.labels = ["Large Cap", "Small Cap", "International Equity",
                       "Fixed Income", "Alternatives", "Cash"]
        return self.labels

    def set_sizes(self, time_horizon, risk_category):
        if time_horizon == 'Short Term' and \
                 risk_category == "Conservative":
            self.sizes = [15, 5, 5, 65, 5, 5]
            return self.sizes
        #     print('yay')
        # else:
        #     print('no')



my_mix = AssetMixes()
testing2 = my_mix.set_sizes(user_th.horizon_category, user_rp.risk_category)
testing = my_mix.set_labels()
print(user_th.horizon_category)


