#1
print([x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)])
#2
try:
    a = 1 / 0
except ZeroDivisionError:
    print('Возникло исключение: ошибка деления на ноль!')
    a = 0
else:
    print('Ветка else вызываетсяб сли не возникло исключения')
finally:
    print('Идем дальше...')
#3
while True:
    a = input()
    try:
        n = int(s)
    except ValueError:
        try:
            n = float(a)
        except:
            print('Это не вещественное число')
        else:
            print(f'Было введено вещественное число: {a}')
            break
        print('Это не целое число')
        print('Повторите ввод')
    else:
        print(f'Было введено целое число: {a}')
        break
#4
def fun(n):
    for x in range(n):
        yield x ** 3 if x % 2 else x **2
g = fun(10)
for k in g:
    print(k)
#5
def fun(n):
    for x in range(n):
        print('before', x)
        yield x * x
        print('after')
g = fun(7)
for k in g:
    print('before k')
    print('k = ', k)
    print('after k')
#6
def fun(n):
    for x in range(n):
        yield x * x
g = fun(4)
for k in range(10):
    try:
        print(next(g))
    except StopIteration:
        break
#7
n = int(input())
def factorial():
    f, k = 1, 1
    while True:
        yield f
        k += 1
        f += k
gf = factorial()
for _ in range(n):
    print(next(gf))
#8
lst = list(map(int, input().split())) # 1 10 100 2 20 200

def summa(lst):
    n = 0
    for i in lst:
        n += i
        yield n
gf = summa(lst)
for i in gf:
    print(i)
#9
def su():
    n = 0
    while True:
        n += 1
        for k in range(n):
            yield n
gf = su()
for i in range(10):
    print(next(gf), end = ' ')