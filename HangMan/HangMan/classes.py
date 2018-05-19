import random
import re
import string
import urllib.request
from bs4 import BeautifulSoup



class Keyword:

    def __init__(self):
        self.keyword = ""
        self.hidden = ""

    @staticmethod
    def initialize_list():
        with urllib.request.urlopen("https://globalnews.ca/world/") as url:
            html = url.read()

        soup = BeautifulSoup(html, "lxml")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        keywords = text[692:2500].split("World\n")
        
        for k in keywords:
            for c in k:
                if c.upper() not in (string.ascii_uppercase+" "):
                    k = k.replace(c, "")

        return keywords


    def assign_new(self, keywords_list):

        self.keyword = keywords_list[random.randint(0, len(keywords_list)-1)].upper()

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


