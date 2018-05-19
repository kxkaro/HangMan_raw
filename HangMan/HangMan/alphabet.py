class Alphabet:

    import string

    def __init__(self):
        self.alphabet = ""
        for c in string.ascii_uppercase: self.alphabet = self.alphabet + c + " "

        self.used_letters = ""


    def remove_letter(self, c):
        self.alphabet = self.alphabet.replace(c.upper() + " ", "")
        
        return self.alphabet


    def update_used(self, c):
        self.used_letters = self.used_letters + c