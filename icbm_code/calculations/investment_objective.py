class InvestmentObjective:
    """Calculates the investment objective score"""

    def __init__(self, objective='', objective_final_score=0,
                 first_answer_score=0, second_answer_score=0):
        """Defines investment objective attributes"""
        self.objective = objective
        self.objective_final_score = objective_final_score
        self.first_answer_score = first_answer_score
        self.second_answer_score = second_answer_score

    # Functions that calculate questions separately
    def calc_first_answer(self, first_answer):
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

    def calc_second_answer(self, second_answer):
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

