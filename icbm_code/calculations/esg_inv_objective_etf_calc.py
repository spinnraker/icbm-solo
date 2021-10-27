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

    # Functions that calculate questions separately
    def calc_first_answer(self, first_answer):
        """Assigns a value to first ESG question"""
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
        """Assigns a value to the second ESG question"""
        if second_answer == 'a':
            self.second_answer_score = 1
        elif second_answer == 'b':
            self.second_answer_score = 2
        elif second_answer == 'c':
            self.second_answer_score = 3
        elif second_answer == 'd':
            self.second_answer_score = 4
        elif second_answer == 'e':
            self.second_answer_score = 5
        else:
            print("You entered an invalid answer")
        return self.second_answer_score

    def calc_third_answer(self, third_answer):
        """Assigns a value to the third ESG question"""
        if third_answer == 'a':
            self.third_answer_score = 1
        elif third_answer == 'b':
            self.third_answer_score = 2
        elif third_answer == 'c':
            self.third_answer_score = 3
        elif third_answer == 'd':
            self.third_answer_score = 4
        elif third_answer == 'e':
            self.third_answer_score = 5
        else:
            print("You entered an invalid answer")
        return self.third_answer_score

    def calc_fourth_answer(self, fourth_answer):
        """Assigns a value to the fourth ESG question"""
        if fourth_answer == 'a':
            self.fourth_answer_score = 1
        elif fourth_answer == 'b':
            self.fourth_answer_score = 2
        elif fourth_answer == 'c':
            self.fourth_answer_score = 3
        elif fourth_answer == 'd':
            self.fourth_answer_score = 4
        elif fourth_answer == 'e':
            self.fourth_answer_score = 5
        else:
            print("You entered an invalid answer")
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
            print('You entered an invalid value')
        return self.first_answer_score

    def calc_io_second_answer(self, second_answer):
        """Assigns a value to second investment objective question"""
        if second_answer == 'a':
            self.second_answer_score = 5
        elif second_answer == 'b':
            self.second_answer_score = 3
        elif second_answer == 'c':
            self.second_answer_score = 1
        else:
            print("You entered an invalid value")
        return self.second_answer_score

    def set_objective(self):
        """Assigns investment objective based on user's input"""
        final_score = self.first_answer_score + self.second_answer_score
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
            self.etf_style = "Balanced"
            self.etf_type = "Growth"
        elif esg_category == "High" and objective == "Growth":
            self.etf_style = "ESG"
            self.etf_type = "Growth"

    def get_etf_style(self):
        return self.etf_style

    def get_etf_type(self):
        return self.etf_type


# my_esg = EnvironmentalSocialGovernance()
# one = my_esg.calc_first_answer('e')
# two = my_esg.calc_second_answer('e')
# three = my_esg.calc_third_answer('e')
# four = my_esg.calc_fourth_answer('e')
#
# my_esg.set_esg_cat()
# total = my_esg.get_est_cat()
# print(total)
