#1
def fu(a = []):
    a.append('abc')
    return a
print(fu())
print(fu())
print(fu())
#2
class A:
    def __init__(self):
        self.even = 0
        self.odd = 1
    def __call__(self):
        self.even += 2
        return self.even
    def __getitem__(self, n):
        self.odd += 2
        return self.odd
    def __repr__(self):
        return str(f'{self.even} / {self.odd}')
    def __str__(self):
        return f'{self.even} / {self.odd}'

a = A()
print(a())
print(a.__getitem__(0)) # == print(a[0])
print(a[0])
print(a)
print(a.__str__())
print(a.__repr__())
#3
class Car:
    color = 'Red'
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def __str__(self):
        return f'Модель: {self.model} с ценой: {self.price}'
obj = Car('UAZ PATRIOT', 1200000)
print(obj.__dict__)
print(obj)
#4
class Obj:
    def __init__(self):
        self.x = 0
        self.y = 1
    def __str__(self):
        lst = []
        for i, j in self.__dict__.items():
            lst.append(str(i)+':'+str(j))
        return ','.join(lst)
obj = Obj()
print(obj)
#5
class Num:
    def __init__(self, number):
        self.number = number
    def __eq__(self, obj):
        return bool(1 - (self.number + obj.number) % 2)
n1 = Num(12)
n2 = Num(123)
print(n1 == n2)
#6
class Gnirts:
    def __init__(self, s):
        self.s = s
    def __gt__(self, obj):
        return len(self.s) > len(obj.s)
    def __str__(self):
        return self.s
s1 = Gnirts('11111111')
s2 = Gnirts('123')
print(min('11111111', '123'))
print(min(s1, s2))
#7
class Num:
    def __init__(self):
        self.x = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.x = 1 - self.x
        return self.x
a = Num()

for i in range(5):
    print(next(a))
#8
class Num:
    def __init__(self):
        self.n = 0
        self.x = 0
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.n += 1
        self.x += self.n
        return self.x
a = Num()
for i in range(15):
    print(next(a), end = ' ')
#9
import itertools
for x in itertools.permutations([1,2,3]):
    print(x, end= ' ')
print()
for x in itertools.combinations([1,2,3,4], 3):
    print(x, end= ' ')
print()
for x in itertools.combinations_with_replacement([1, 2, 3, 4], 3):
    print(x, end=' ')
print()
x = itertools.cycle([1,2,3,4])
for _ in range(10):
    print(next(x), end= ' ')
print()
for x in itertools.chain([1,2,3], 'abc', {10:100, 20:200, 30:300})
    print(x, end=' ')
#10
import itertools
lst = []
lst2 = []
n = str(input())
for x in itertools.permutations(['a','a','b','b']):
    lst.append(''.join(x))
l = set(lst)
for x in itertools.permutations(n):
    lst2.append(''.join(x))
l2 = set(lst2)
print(l)
print(l2)
