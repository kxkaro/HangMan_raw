import os
from alphabet import *
from keyword import *
from score import *

game_on = True
score = Score(5)

while game_on:

    alphabet = Alphabet()
    keyword = Keyword.pick()
    hiddenKeyword = Keyword.hide(keyword)

    while score.current_score > 0 and hiddenKeyword.upper() != keyword.upper():
        print("Total score: " + str(score.total_score))
        print(str(score.current_score) + " mistakes to hang!")
        print(hiddenKeyword)
        print(alphabet.alphabet)
        c = input("Pick a letter from the alphabet: ")

        if len(c) != 1: 
            os.system('cls')
            print("You can pick only one letter!")
            continue

        elif c in alphabet.used_letters:
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

            alphabet.alphabet = alphabet.remove_letter(c)
            alphabet.update_used(c)


    if hiddenKeyword.upper() == keyword.upper():
        os.system('cls')
        score.increase_total(score.current_score)
        score.reset_current()
        
        print("You won! Next round!")

    elif score.current_score == 0:
        print("Game over!")
        print("Your total score is " + str(score.total_score))
        game_on = False
        