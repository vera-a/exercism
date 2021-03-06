import random
import string

class Robot():
    def __init__(self):
        self.name = self.generate_name()


    def generate_name(self):
        random.seed()
        random.random()
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        name = ''.join(letters + digits)
        return name



    def reset(self):
        self.name = self.generate_name()
