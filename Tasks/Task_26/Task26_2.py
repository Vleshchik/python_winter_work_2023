def dis(self):
    for attr in self.__dict__:
        print(f"{attr}: {self.__dict__[attr]}")

Par = type('Par', (), {'dis': dis})

p = Par()
p.x = 10
p.y = 20
p.dis()