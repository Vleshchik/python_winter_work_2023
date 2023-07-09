#1
import re
pods = input() #ос
text = input() #Косой косой косил волос на осине
print(re.findall(fr'\b\w+{pods}\w+\b', text))
#2
def fu(*args, **kwargs):
    res = []
    res2 = ''
    for i in args:
        if type(i) == str:
            res.append(i)
            res2 += i
    for i in kwargs:
        if type(kwargs[i]) == str:
            res.append(kwargs[i])
            res2 += kwargs[i]
    return ''.join(res), res2
print(fu('qwerty', 's', 'abc', a = 3, b = 'def'))
#3
def deco(func):
    def wrapper(*args):
        z =  func(*args)
        res = ''.join(args)
        return res
    return wrapper
@deco
def a(*args):
    return
print(a('xxx', 'yyy', 'zzz'))
@deco
def b(x, y):
    return len(x) + len(y)
print(b('hello', 'world'))
#4
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cur_money = self.money
        #print(self.name, self.money)
    def give_money(self, other, x_money):
        if self.cur_money >= x_money:
            other.cur_money += x_money
            self.cur_money -= x_money
        else:
            print('Недостаточно средств')
    def info(self):
        print(self.name,self.money, self.cur_money)
    def set_money(self, x):
        self.cur_money += x
    def get_money(self):
        return self.cur_money

a = Person('Pete', 200)
b = Person('Nick', 300)
c = Person('Jack', 5000)
print(a.money, b.money)
print(a.name, b.name)
a.give_money(b, 100)
a.info(), b.info()
a.set_money(200)
b.set_money(100)
c.give_money(a, 200)
c.give_money(b, 200)
a.info(), b.info(), c.info()
print(a.get_money())
a.give_money(b, 600)
#5
class Warehouse:
    def __init__(self, name_of_goods, number_of_goods):
        self.name_of_goods = name_of_goods
        self.number_of_goods = number_of_goods
        self.current_number_of_goods = self.number_of_goods
        #print(self.name, self.money)
    def info(self):
        print(self.name_of_goods, self.number_of_goods, self.current_number_of_goods)
    def set_goods(self, x):
        self.current_number_of_goods += x
    def get_goods(self):
        return self.current_number_of_goods
a = Warehouse('wood', 3000)
b = Warehouse('iron', 1000)
c = Warehouse('glass', 2000)
d = Warehouse('paper', 500)
a.info(), b.info(), c.info(), d.info()