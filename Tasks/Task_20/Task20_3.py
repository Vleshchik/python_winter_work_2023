class Num_Alph:
    def __init__(self):
        self.x = 1
        self.l = 'A'
        self.n = 0
        self.c = 1
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.x == 1:
                if self.n < 26:
                    self.x = 1 - self.x
                    self.n += 1
                    return self.n
                else:
                    self.n = 0
                    self.x == 1
                    self.l = 'A'
            else:
                if self.n < 27:
                    self.x = 1 - self.x
                    self.l = chr(64 + self.n)
                    return self.l
                else:
                    self.n = 0
                    self.x == 1
                    self.l = 'A'
a = Num_Alph()
for i in range(120):
    print(next(a), end=',')