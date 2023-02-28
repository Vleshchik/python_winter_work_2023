class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    def set_colour(self, x):
        self.colour = x
    def colour_info(self):
        print(self.colour)
    def set_square(self, x):
        self.square = x
    def square_info(self):
        print(self.square)
a = Shape('синий', 10)
b = Shape('красный', 15)
c = Shape('желтый', 5)
a.colour_info(), b.colour_info(), c.colour_info()
a.square_info(), b.square_info(), c.square_info()
a.set_colour('лазурный'), b.set_colour('алый'), c.set_colour('персиковый')
a.colour_info(), b.colour_info(), c.colour_info()

