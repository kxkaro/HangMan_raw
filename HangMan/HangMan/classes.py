import random
import re
import string

class Keyword:

    def __init__(self):
        self.keyword = ""
        self.hidden = ""


    def assign_new(self):

        keywords = ['abracadabra', 
                 'nonsense', 
                 'gamification', 
                 'extraordinary', 
                 'this game is stupid']

        self.keyword = keywords[random.randint(0, len(keywords)-1)].upper()

        self.hidden = self.keyword

        #while ''.join(set(keyword)).replace(" ", "") != ".":
        for c in self.hidden:
            if c in string.ascii_uppercase: self.hidden = self.hidden.replace(c, '.')


    def update(self, c):
        indexes = [m.start() for m in re.finditer(c.upper(), self.keyword)]

        for i in range(len(indexes)): 
            self.hidden = self.hidden[:indexes[i]] + c.upper() + self.hidden[indexes[i]+1:]


class Alphabet:

    def __init__(self):
        self.available = ""
        self.used = ""

    
    def reset(self):
        self.available = ""
        for c in string.ascii_uppercase: self.available = self.available + c + " "
        self.used = ""


    def update(self, c):
        self.available = self.available.replace(c.upper() + " ", "")
        self.used = self.used + c

class Score:
    
    def __init__(self, max_trials):
        self.current_score = max_trials
        self.total_score = 0


    def decrease_current(self):
        self.current_score -=1


    def update(self):
        self.total_score += self.current_score
        self.current_score = 5


