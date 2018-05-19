class Keyword:

    import random
    import re

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