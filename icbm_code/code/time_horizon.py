class TimeHorizon:
    """Calculates Time Horizon Score"""

    def __init__(self, time_score=0, horizon_category='', answer=''):
        """Initialize time attribute."""
        self.answer = answer
        self.time_score = time_score
        self.horizon_category = horizon_category

    def get_time(self):
        """Return time score"""
        return f'Time horizon score: {self.time_score}' \
               f'\nHorizon Category: {self.horizon_category}'

    def set_time(self, user_answer):
        """Assigns time horizon scored based on user's input"""
        if user_answer == 'a':
            self.time_score = 1
            self.horizon_category = 'Ultra-Short Term'
        elif user_answer == 'b':
            self.time_score = 2
            self.horizon_category = 'Short Term'
        elif user_answer == 'c':
            self.time_score = 3
            self.horizon_category = 'Intermediate Term'
        elif user_answer == 'd':
            self.time_score = 4
            self.horizon_category = 'Long Term'
        else:
            print("You entered an invalid value.")

