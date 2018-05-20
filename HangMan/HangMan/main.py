import os
import classes as cls

#if cls.Keyword.keywords is None:
cls.Keyword.initialize_list()

keywords = cls.Keyword.keywords_list
keyword = cls.Keyword()
alphabet = cls.Alphabet()
score = cls.Score(3)
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

        if len(c) != 1: 
            os.system('cls')
            print("You can pick only one letter!")
            continue

        elif c in alphabet.used:
            os.system('cls')
            print("You've already used this letter!")
            continue

        else:
            os.system('cls')
            if c.upper() in keyword.keyword: 
                keyword.update(c)
                print("Well done!")

            else: 
                score.decrease_current()
                print("Wrong!")

            alphabet.update(c)


    if keyword.hidden == keyword.keyword:
        os.system('cls')
        #score.increase_total(score.current_score)
        score.update()

        input(keyword.keyword + "\n\nGood job! Next round!")
        os.system('cls')

    elif score.current_score == 0:
        print("Game over!")
        print("Your total score is " + str(score.total_score))
        game_on = False
        