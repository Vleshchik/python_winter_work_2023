#1
lst = [1, 2, 3, 4, 5]
for x in lst:
    lst.pop(0)
print(lst)
#2
try:
    file = open('ok123.txt', 'r')
except FileNotFoundError as e:
    print(FileNotFoundError, e)
except Exception as e:
    print(Exception, e)
#3
def divide(x, y):
    try:
        out = x // y
    except:
        try:
            import math
            out = math.inf * x / abs(x)
        except:
            out = None
        finally:
            return out
print(divide(15, 3))
print(divide(15, 0))
print(divide(-15, 3))
print(divide(0, 0))
#4
try:
    raise Exception("Что-то пошло не так")
except Exception as e:
    print('Message:' + str(e))
#5
def validate(name):
    if len(name) < 10:
        raise ValueError

try:
    name = input("Введите имя:")
    validate(name)
except ValueError:
    print("Имя слишком короткое")
#6
class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name) < 10:
        raise NameTooShortError
try:
    validate(input())
except NameTooShortError:
    print("Name too short error")
#7
def fun_get1():
    yield 'Red'
    yield 'Green'
    yield 'Blue'
def fun_gen2():
    yield 'Round'
    yield from fun_get1()
    yield 'Square'
print(*fun_gen2())
#8
def integers(n):
    for i in range(1, n +1):
        yield i
def evens(iterable):
    for i in iterable:
        if not i % 2:
            yield i
def squared(iterable):
    for k in iterable:
        yield k * k
chain = squared(evens(integers(10)))
print(*chain)
#9
def iii():
    x = ord('а')
    z = ord('я')
    yield from range(x, z + 1)
def ev(ite):
    for i in ite:
        yield chr(i)
chain = ev(iii())
print(*chain)
#10
def func(n):
    print("func1", n)
    n -= 1
    if n > 0:
        func(n)
    print('func2', n)
    return
func(10)
#11
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(1))
print(fact(2))
print(fact(3))
#12
def fa(n):
    return 1 if n == 0 else n * fa(n - 1)
print(fa(1))
#13
def triangle(n):
    if n >= 1:
        triangle(n - 1)
    print('*' * n)

triangle(int(input()))
#14
def triangle(n):
    print('*' * n)
    if n >= 1:
        triangle(n - 1)
triangle(int(input()))
#15
def sumn(n): #числа трибоначчи
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        return sumn(n - 3) + sumn(n - 2) + sumn(n - 1)
k = int(input())
for i in range(1, k+1):
    print(sumn(i))
#16
def sumn(n): #числа фибоначчи
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sumn(n - 2) + sumn(n - 1)
k = int(input())
for i in range(1, k+1):
    print(sumn(i))