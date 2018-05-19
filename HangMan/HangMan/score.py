class Score:
    
    def __init__(self, max_trials):
        self.current_score = max_trials
        self.total_score = 0


    def decrease_current(self):
        self.current_score -=1


    def reset_current(self):
        self.current_score = 5


    def increase_total(self, i):
        self.total_score += i