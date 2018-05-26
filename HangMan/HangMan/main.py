import os 
from cls.keyword import *
from cls.alphabet import *
from cls.score import *


#if cls.Keyword.keywords is None:
Keyword.initialize_list()

keywords = Keyword.keywords_list
keyword = Keyword()
alphabet = Alphabet()
score = Score(3)
game_on = True

while game_on:

    keyword.assign_new(keywords)
    alphabet.reset()

    while score.current_score > 0 and keyword.hidden != keyword.keyword:
        print("Total score: " + str(score.total_score))
        print(str(score.current_score) + " mistakes to hang!")
        print(keyword.hidden)
        print(alphabet.available)
        c = input("Pick a letter from the alphabet: ")
        os.system('cls')

        if len(c) != 1: 
            print("You can pick only one letter!")
            continue

        elif c in alphabet.used:
            print("You've already used this letter!")
            continue

        else:
            if c.upper() in keyword.keyword: 
                keyword.update(c)
                print("Well done!")

            else: 
                score.decrease_current()
                print("Wrong!")

            alphabet.update(c)


    if keyword.hidden == keyword.keyword:
        os.system('cls')
        score.update()

        input(keyword.keyword + "\n\nGood job! Next round!")
        os.system('cls')

    elif score.current_score == 0:
        print("Game over!")
        print("Your total score is " + str(score.total_score))
        game_on = False
        