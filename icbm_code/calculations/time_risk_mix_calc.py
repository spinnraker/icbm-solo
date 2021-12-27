class TimeRiskMixCalculator:
    """Calculates Mix Asset based on Time horizon and risk profile"""

    # Time Horizon functions
    def __init__(self, time_score=0, horizon_category='', risk_score=0,
                 risk_category='', first_answer_score=0,
                 second_answer_score=0, third_answer_score=0,
                 fourth_answer_score=0, asset_mix=''):
        """Initialize time attributes."""
        self.time_score = time_score
        self.horizon_category = horizon_category
        self.risk_score = risk_score
        self.risk_category = risk_category
        self.first_answer_score = first_answer_score
        self.second_answer_score = second_answer_score
        self.third_answer_score = third_answer_score
        self.fourth_answer_score = fourth_answer_score
        self.asset_mix = asset_mix

    def set_time(self, user_answer):
        """Assigns time horizon scored based on user's input"""
        answers = {'a': {'score': 1, 'category': 'Short Term'},
                   'b': {'score': 2, 'category': 'Intermediate Term'},
                   'c': {'score': 3, 'category': "Long Term"}}

        self.time_score = answers[user_answer]['score']
        self.horizon_category = answers[user_answer]['category']

    def get_time(self):
        """Return time score"""
        return f'\nTime Horizon Score: {self.time_score}' \
               f'\nHorizon Category: {self.horizon_category}'

    def get_th_cat(self):
        return self.horizon_category

    # Risk profile functions

    def calc_first_answer(self, first_answer):
        """Assigns a value to first Risk question"""
        answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.first_answer_score = answers[first_answer]
        return self.first_answer_score

    def calc_second_answer(self, second_answer):
        """Assigns a value to second Risk question"""
        answers = {'a': 2, 'b': 3, 'c': 4, 'd': 5}
        self.second_answer_score = answers[second_answer]
        return self.second_answer_score

    def calc_third_answer(self, third_answer):
        """Assigns a value to third Risk question"""
        answers = {'a': 1, 'b': 3, 'c': 5}
        self.third_answer_score = answers[third_answer]
        return self.third_answer_score

    def calc_fourth_answer(self, fourth_answer):
        """Assigns a value to third Risk question"""
        answers = {'a': 1, 'b': 3, 'c': 5}
        self.fourth_answer_score = answers[fourth_answer]
        return self.fourth_answer_score

    # Set risk score
    def set_risk_score(self):
        total_risk_score = self.first_answer_score + self.second_answer_score
        total_risk_score += self.third_answer_score + self.fourth_answer_score
        if total_risk_score <= 8:
            self.risk_category = "Conservative"
        elif (total_risk_score == 9) or (total_risk_score <= 15):
            self.risk_category = "Moderate"
        else:
            self.risk_category = "Aggressive"
        self.risk_score = total_risk_score

    def get_risk_category(self):
        return f'Risk Score: {self.risk_score} ' \
               f'\nRisk Category: {self.risk_category}'

    def get_risk_cat(self):
        return self.risk_category

    # Calculate asset mix
    def calculate_mix(self, horizon_answer, risk_answer):
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

    def get_mix(self):
        return self.asset_mix

