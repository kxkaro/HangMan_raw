

import random
import string
import re
import os

class Keyword:

    def pick():
        keywords = ['abracadabra', 
                 'nonsense', 
                 'gamification', 
                 'extraordinary', 
                 'this game is stupid']

        return keywords[random.randint(0, len(keywords)-1)]


    def hide(keyword):
        keyword = keyword.upper()

        #while ''.join(set(keyword)).replace(" ", "") != ".":
        for c in keyword:
            if c in string.ascii_uppercase: keyword = keyword.replace(c, '.')
    
        return keyword


    def update_hidden(keyword, hiddenKeyword, c):
        indexes = [m.start() for m in re.finditer(c.upper(), keyword.upper())]

        for i in range(len(indexes)): 
            hiddenKeyword = hiddenKeyword[:indexes[i]] + c.upper() + hiddenKeyword[indexes[i]+1:]
    
        return hiddenKeyword


class Alphabet:

    def __init__(self):
        self.alphabet = ""
        for c in string.ascii_uppercase: self.alphabet = self.alphabet + c + " "

        self.used_letters = ""


    def remove_letter(self, c):
        self.alphabet = self.alphabet.replace(c.upper() + " ", "")
        
        return self.alphabet
    

    def update_used(self, c):
        self.used_letters = self.used_letters + c


class Score:
    
    def __init__(self):
        self.current_score = 5
        self.total_score = 0

    def decrease_current(self):
        self.current_score -=1

    def reset_current(self):
        self.current_score = 5

    def increase_total(self, i):
        self.total_score += i


#Main
game_on = True
score = Score()

while game_on:

    alphab = Alphabet()
    keyword = Keyword.pick()
    hiddenKeyword = Keyword.hide(keyword)

    while score.current_score > 0 and hiddenKeyword.upper() != keyword.upper():
        print("Total score: " + str(score.total_score))
        print("Tries: " + str(score.current_score))
        print(hiddenKeyword)
        print(alphab.alphabet)
        c = input("Pick a letter from the alphabet: ")

        if len(c) != 1: 
            os.system('cls')
            print("You can pick only one letter!")
            continue

        elif c in alphab.used_letters:
            os.system('cls')
            print("You've already used this letter!")
            continue

        else:
            os.system('cls')
            if c.upper() in keyword.upper(): 
                hiddenKeyword = Keyword.update_hidden(keyword, hiddenKeyword, c)
                print("Well done!")

            else: 
                score.decrease_current()
                print("Wrong!")

            alphab.alphabet = alphab.remove_letter(c)
            alphab.update_used(c)


    if hiddenKeyword.upper() == keyword.upper():
        os.system('cls')
        score.increase_total(score.current_score)
        score.reset_current()
        
        print("You won! Next round!")

    elif score.current_score == 0:
        print("Game over!")
        print("Your total score is " + str(score.total_score))
        game_on = False
        