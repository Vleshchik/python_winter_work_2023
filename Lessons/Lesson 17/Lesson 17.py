class Pet:
    def __init__(self, name, weight, level_of_hungriness):
        self.name = name
        self.weight = weight
        self.level_of_hungriness = level_of_hungriness
    def info(self):
        print(self.name, self.weight, self.level_of_hungriness)
    def hungry(self):
        if self.level_of_hungriness > 10:
            print('Питомец сыт')
        elif self.level_of_hungriness < 5:
            print('Питомец голоден')
    def feed(self, x):
        self.level_of_hungriness += x
        self.info()
a = Pet('Ларда', 21, 11)
b = Pet('Райф', 35, 7)
c = Pet('Джови', 17, 3)
a.info(), b.info(), c.info()
a.hungry(), b.hungry(), c.hungry()
a.feed(10), b.feed(10),c.feed(10)
a.hungry(), b.hungry(), c.hungry()
class Dog(Pet):
    def voice(self):
        print('bark')
class Cat(Pet):
    def voice(self):
        print('meow')
    def hungry(self):
        if self.level_of_hungriness >= 8:
            print('Питомец сыт')
        elif self.level_of_hungriness <= 3:
            print('Питомец голоден')
l = Dog('Ларда', 21, 11)
l.voice()
l.info()

