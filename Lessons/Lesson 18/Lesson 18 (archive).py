#1
class Shape:
    def __init__(self, perimeter, colour, square):
        self.perimeter = perimeter
        self.colour = colour
        self.square = square
    def peri_info(self):
        print(self.perimeter)
    def set_colour(self, x):
        self.colour = x
    def colour_info(self):
        print(self.colour)
    def set_square(self, x):
        self.square = x
    def square_info(self):
        print(self.square)
s = Shape(10, 'red', 10)
print(s.perimeter, s.colour)
z = Shape(20, 'blue', 20)
z.colour_info(), z.peri_info(), z.square_info()
#2
class Student:
    lst = []
    def __init__(self, name):
        self.name = name
        Student.lst.append(self.name)
    def show(self):
        print(self.name)

s1 = Student('Emma')
s2 = Student('Nick')
s1.show()
s2.show()
print(Student.lst)
print(isinstance(s1, Student))
print(s1.__class__)
print(dir(s1))
#3
class Tree:
    def __init__(self, kind, height):
        self.kind = kind
        self.age = 0
        self.height = height
    def grow(self):
        self.age += 1

class FruitTree(Tree):
    def __init__(self, kind, height):
        super().__init__(kind, height)
    def give_fruits(self, x = 20):
        print("Collected {} kg of {}s".format(x, self.kind))
f_tree = FruitTree('Apple', 0.7)
f_tree.col = 'Red'
s_tree = Tree('oak', 3)
orange = FruitTree('Orange', 0.7)
#4
class Shape:
    def __init__(self, colour = 'red', perimeter = 0):
        self.perimeter = perimeter
        self.colour = colour
    def peri_info(self):
        print(self.perimeter)
    def set_colour(self, x):
        self.colour = x
    def colour_info(self):
        print(self.colour)
class Triangle(Shape):
    def tri_check(a, b, c):
        if a > 0 and b > 0 and c > 0:
            if a + b > c and b + c > a and a + c > b:
                return True
    def __init__(self, a, b, c):
        super().__init__()
        if Triangle.tri_check(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            print('It is not a trianle')
    def peri(self):
        return self.a + self.b + self.c
class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    def peri(self):
        return 2 * (self.a + self.b)
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

z = Triangle(3, 4, 5)
print(z.peri())
s = Square(4)
print(s.peri())