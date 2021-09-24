class InvestmentObjective:
    """Calculates the investment objective score"""

    def __init__(self, objective='', objective_score=0):
        """Defines investment objective attributes"""
        self.objective = objective
        self.objective_score = objective_score

    def get_objective(self):
        """Displays user's investment objective"""
        return self.objective

    def set_objective(self, first_answer, second_answer):
        """Assigns investment objective based on user's input"""
        final_score = first_answer + second_answer
        if final_score <= 4:
            self.objective = "Income"
        elif (final_score == 5) or (final_score < 7):
            self.objective = "Balanced"
        else:
            self.objective = "Growth"


inv_obj = InvestmentObjective()

inv_obj.set_objective(1, 1)
print(inv_obj.get_objective())