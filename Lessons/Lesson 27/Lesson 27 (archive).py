#1
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
#2

def dis(self):
    return print(Par.__dict__)
Par = type('Par', (), {'dis':dis, 'x': 123})
a = Par()
a.dis()

#3
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f' vec with coor ({self.x}, {self.y})'
    def __repr__(self):
        return f' vec ({self.x},{self.y})'

v = Vector(2,3)
print(str(v))
print(repr(v))
print(v)
#4