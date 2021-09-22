class TimeHorizon:
    """Calculates Time Horizon Score"""
    time_score = 0

    def __init__(self, time_score=0, answer=''):
        """Initialize time attribute."""
        self.answer = answer
        self.time_score = time_score

    def get_time(self):
        """Return time score"""
        return f'Time horizon score: {self.time_score}'

    def set_time(self, user_answer):
        """Assigns time horizon scored based on user's input"""
        if user_answer == 'a':
            self.time_score = 1
        elif user_answer == 'b':
            self.time_score = 2
        elif user_answer == 'c':
            self.time_score = 3
        elif user_answer == 'd':
            self.time_score = 4
        else:
            print("You entered an invalid value.")


