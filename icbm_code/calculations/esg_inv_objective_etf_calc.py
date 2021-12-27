class ESGInvestmentObjectiveETFCalculator:
    """Calculates the ETFs to show based on ESG preference and Investment
    Objective"""

    def __init__(self, esg_score=0, esg_category='', first_answer_score=0,
                 second_answer_score=0, third_answer_score=0,
                 fourth_answer_score=0, objective='', objective_final_score=0,
                 io_first_answer_score=0, io_second_answer_score=0, etf_type="",
                 etf_style=""):
        """Defines ESG class attributes"""
        # ESG attributes
        self.esg_score = esg_score
        self.esg_category = esg_category
        self.first_answer_score = first_answer_score
        self.second_answer_score = second_answer_score
        self.third_answer_score = third_answer_score
        self.fourth_answer_score = fourth_answer_score
        # Investment Objective attributes
        self.objective = objective
        self.objective_final_score = objective_final_score
        self.io_first_answer_score = io_first_answer_score
        self.io_second_answer_score = io_second_answer_score
        self.etf_type = etf_type
        self.etf_style = etf_style

    def calc_first_answer(self, first_answer):
        """Assigns a value to first ESG question"""
        answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.first_answer_score = answers[first_answer]
        return self.first_answer_score

    def calc_second_answer(self, second_answer):
        """Assigns a value to the second ESG question"""
        answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.second_answer_score = answers[second_answer]
        return self.second_answer_score

    def calc_third_answer(self, third_answer):
        """Assigns a value to the third ESG question"""
        answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.third_answer_score = answers[third_answer]
        return self.third_answer_score

    def calc_fourth_answer(self, fourth_answer):
        """Assigns a value to the fourth ESG question"""
        answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.first_answer_score = answers[fourth_answer]
        return self.fourth_answer_score

    # Calculates ESG category based on total score
    def set_esg_cat(self):
        """Assigns ESG score based on user's input"""
        final_esg_score = self.first_answer_score + self.second_answer_score
        final_esg_score += self.third_answer_score + self.fourth_answer_score
        if final_esg_score <= 8:
            self.esg_category = "Low"
        elif (final_esg_score == 9) or (final_esg_score <= 15):
            self.esg_category = "Medium"
        else:
            self.esg_category = "High"
        self.esg_score = final_esg_score

    def get_esg_cat_score(self):
        """Displays user's ESG result and category"""
        return f'\nESG Score: {self.esg_score}' \
               f'\nESG category: {self.esg_category}'

    def get_esg_cat(self):
        return self.esg_category

    # Calculate Investment Objective
    def calc_io_first_answer(self, first_answer):
        """Assigns a value to first investment objective question"""
        answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.io_first_answer_score  = answers[first_answer]
        return self.io_first_answer_score

    def calc_io_second_answer(self, second_answer):
        """Assigns a value to second investment objective question"""
        answers = {'a': 5, 'b': 3, 'c': 1}
        self.io_second_answer_score = answers[second_answer]
        return self.io_second_answer_score

    def set_objective(self):
        """Assigns investment objective based on user's input"""
        final_score = self.io_first_answer_score + self.io_second_answer_score
        if final_score <= 4:
            self.objective = "Income"
        elif (final_score == 5) or (final_score <= 6):
            self.objective = "Balanced"
        else:
            self.objective = "Growth"
        self.objective_final_score = final_score

    def get_objective(self):
        """Displays user's investment objective"""
        return f'\nInvestment Score: {self.objective_final_score} ' \
               f'\nInvestment objective: {self.objective}'

    def get_cat(self):
        return self.objective

    def select_etfs(self, esg_category, objective):
        # esg_category = self.esg_category
        # objective = self.objective
        if esg_category == "Low" and objective == "Income":
            self.etf_style = "Non-ESG"
            self.etf_type = "Value"
        elif esg_category == "Low" and objective == "Balanced":
            # self.etf_table = "traditionalBalancedDB"
            self.etf_style = "Non-ESG"
            self.etf_type = "Balanced"
        elif esg_category == "Low" and objective == "Growth":
            self.etf_style = "Non-ESG"
            self.etf_type = "Growth"
            # This portion needs to be updated once we figure out how to show both
        elif esg_category == "Medium" and objective == "Income":
            self.etf_style = "ESG"
            self.etf_type = "Value"
        elif esg_category == "Medium" and objective == "Balanced":
            self.etf_style = "ESG"
            self.etf_type = "Balanced"
        elif esg_category == "Medium" and objective == "Growth":
            self.etf_style = "ESG"
            self.etf_type = "Growth"
        elif esg_category == "High" and objective == "Income":
            self.etf_style = "ESG"
            self.etf_type = "Value"
        elif esg_category == "High" and objective == "Balanced":
            self.etf_style = "ESG"
            self.etf_type = "Growth"
        elif esg_category == "High" and objective == "Growth":
            self.etf_style = "ESG"
            self.etf_type = "Growth"

    def get_etf_style(self):
        return self.etf_style

    def get_etf_type(self):
        return self.etf_type
