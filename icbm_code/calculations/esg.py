class EnvironmentalSocialGovernance:
    """Calculates the ESG score"""

    def __init__(self, esg_score=0, esg_category='', first_q_score=0,
                 second_q_score=0, third_q_score=0, fourth_q_score=0):
        self.esg_score = esg_score
        self.esg_category = esg_category
        self.first_q_score = first_q_score
        self.second_q_score = second_q_score
        self.third_q_score = third_q_score
        self.fourth_q_score = fourth_q_score

    # Functions that calculate questions separately
    def calc_first_answer(self, f_answer):
        """Assigns a value to first ESG question"""
        if f_answer == 'a':
            self.first_q_score = 1
        elif f_answer == 'b':
            self.first_q_score = 2
        elif f_answer == 'c':
            self.first_q_score = 3
        elif f_answer == 'd':
            self.first_q_score = 4
        elif f_answer == 'e':
            self.first_q_score = 5
        else:
            print("You entered an invalid answer")
        return self.first_q_score

    def calc_second_answer(self, s_answer):
        """Assigns a value to the second ESG question"""
        if s_answer == 'a':
            self.second_q_score = 1
        elif s_answer == 'b':
            self.second_q_score = 2
        elif s_answer == 'c':
            self.second_q_score = 3
        elif s_answer == 'd':
            self.second_q_score = 4
        elif s_answer == 'e':
            self.second_q_score = 5
        else:
            print("You entered an invalid answer")
        return self.second_q_score

    def calc_third_answer(self, t_answer):
        """Assigns a value to the third ESG question"""
        if t_answer == 'a':
            self.third_q_score = 1
        elif t_answer == 'b':
            self.third_q_score = 2
        elif t_answer == 'c':
            self.third_q_score = 3
        elif t_answer == 'd':
            self.third_q_score = 4
        elif t_answer == 'e':
            self.third_q_score = 5
        else:
            print("You entered an invalid answer")
        return self.third_q_score

    def calc_fourth_answer(self, fourth_answer):
        """Assigns a value to the fourth ESG question"""
        if fourth_answer == 'a':
            self.fourth_q_score = 1
        elif fourth_answer == 'b':
            self.fourth_q_score = 2
        elif fourth_answer == 'c':
            self.fourth_q_score = 3
        elif fourth_answer == 'd':
            self.fourth_q_score = 4
        elif fourth_answer == 'e':
            self.fourth_q_score = 5
        else:
            print("You entered an invalid answer")
        return self.fourth_q_score

    # Calculates ESG category based on total score
    def set_esg_cat(self):
        total_esg_score = self.first_q_score + self.second_q_score + \
                          self.third_q_score + self.fourth_q_score
        if total_esg_score <= 8:
            self.esg_category = "Low"
        elif (total_esg_score == 9) or (total_esg_score <= 15):
            self.esg_category = "Medium"
        else:
            self.esg_category = "High"


# my_esg = ESG()
#
# total = my_esg.calc_fourth_answer('a')
# print(total)
