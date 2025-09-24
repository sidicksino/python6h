import random

class Dic:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
    
dic = Dic()
print(dic.roll())