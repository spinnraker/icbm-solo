class TimeRiskMixCalculator:
    """Calculates Mix Asset based on Time horizon and risk profile"""

    # Time Horizon functions
    def __init__(self, time_score=0, horizon_category='', risk_score=0,
                 risk_category='', first_answer_score=0,
                 second_answer_score=0, third_answer_score=0,
                 fourth_answer_score=0, asset_mix=""):
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
        if user_answer == 'a':
            self.time_score = 1
            self.horizon_category = 'Short Term'
        elif user_answer == 'b':
            self.time_score = 2
            self.horizon_category = 'Intermediate Term'
        elif user_answer == 'c':
            self.time_score = 3
            self.horizon_category = 'Long Term'
        else:
            print("You entered an invalid value.")

    def get_time(self):
        """Return time score"""
        # return self.horizon_category
        return f'\nTime Horizon Score: {self.time_score}' \
               f'\nHorizon Category: {self.horizon_category}'

    def get_th_cat(self):
        return self.horizon_category

    # Risk profile functions

    def calc_first_answer(self, first_answer):
        """Assigns a value to first Risk question"""
        if first_answer == 'a':
            self.first_answer_score = 1
        elif first_answer == 'b':
            self.first_answer_score = 2
        elif first_answer == 'c':
            self.first_answer_score = 3
        elif first_answer == 'd':
            self.first_answer_score = 4
        elif first_answer == 'e':
            self.first_answer_score = 5
        else:
            print("You entered an invalid answer")
        return self.first_answer_score

    def calc_second_answer(self, second_answer):
        """Assigns a value to second Risk question"""
        if second_answer == 'a':
            self.second_answer_score = 2
        elif second_answer == 'b':
            self.second_answer_score = 3
        elif second_answer == 'c':
            self.second_answer_score = 4
        elif second_answer == 'd':
            self.second_answer_score = 5
        else:
            print("You entered an invalid answer")
        return self.second_answer_score

    def calc_third_answer(self, third_answer):
        """Assigns a value to third Risk question"""
        if third_answer == 'a':
            self.third_answer_score = 1
        elif third_answer == 'b':
            self.third_answer_score = 3
        elif third_answer == 'c':
            self.third_answer_score = 5
        else:
            print("You entered an invalid answer")
        return self.third_answer_score

    def calc_fourth_answer(self, fourth_answer):
        """Assigns a value to third Risk question"""
        if fourth_answer == 'a':
            self.fourth_answer_score = 1
        elif fourth_answer == 'b':
            self.fourth_answer_score = 3
        elif fourth_answer == 'c':
            self.fourth_answer_score = 5
        else:
            print("You entered an invalid answer")
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

