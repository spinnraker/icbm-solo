class ESG:
    """Calculates the ESG score"""

    def __init__(self, esg_score=0, esg_percentage='', first_q_score=0,
                 second_q_score=0, third_q_score=0, fourth_q_score=0):
        self.esg_score = esg_score
        self.esg_percentage = esg_percentage
        self.first_q_score = first_q_score
        self.second_q_score = second_q_score
        self.third_q_score = third_q_score
        self.fourth_q_score = fourth_q_score

    # Functions that calculate questions separately
    def calc_first_q(self, f_answer):
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

    def calc_second_q(self, s_answer):
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


my_esg = ESG()

total = my_esg.calc_first_q('d')
print(total)


