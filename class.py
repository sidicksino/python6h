# class person:
#     def __init__(self, name):
#         self.name = name
    
#     def talk(self):
#         print(f"Hi, I'm {self.name}")

# sidick = person("Sidick Abdoulaye")
# sidick.talk()

# nariman = person("Nariman Osman")
# nariman.talk()


# inheritance 
class Mammal():
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_annoying(self):
        print("Be Annoying")

cat1 = Cat()
cat1.walk

