#1
import datetime, locale
locale.setlocale(locale.LC_ALL, 'ru')
a = datetime.datetime.today() + datetime.timedelta(days=14)
print(a)
c = datetime.timedelta(days=1)
for _ in range(10):
    a+=c
    print(a.strftime('%A %d, %B %Y'))
#2
import calendar
year, month = tuple(map(int, input().split()))
print(calendar.calendar(year))
#3
def flip_flop(x):
    return 'flip' if x == 'flop' else 'flop'
print(flip_flop('flip'))
#4
def fu_1_0(x):
    return 0 if x == 1 else 1
x = 0
for i in range(10):
    print((x := fu_1_0(x)))
#5
print([x ** 2 for x in range(0, 50) if x % 7 == 0])
#6
import time
t0 = time.time()
s = []
for i in range(1000):
    s.append(i ** 3)
print(s)
t1 = time.time()
print(list(map(lambda x: x ** 3, range(0, 1000))))
t2 = time.time()
print([x ** 3 for x in range(1000)])
t3 = time.time()
print(t1 - t0, t2 - t1, t3 - t2)
#7
print([x for x in range(100) if x % 3 == 0])
#8
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)
#9
from string import ascii_letters
letters = 'hыtфтrцзq'
is_eng = [f'{ltr}- ДА' if ltr in ascii_letters else f'{ltr}-НЕТ' for ltr in letters]
print(is_eng)
#10
letters = 'vdwufbwrobnvdwcsdvgierghacnrbgifjdqwpjсйцвтшмуаикетцузйавьтсиыфмзукщмоцвимйзуш'
let = 'aeiouyёуеыаоэяию'
is_vowel = [f'{ltr}- гласная' if ltr in let else f'{ltr}-согласная' for ltr in letters]
print(is_vowel)
#11
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
def get_price(price):
    return price if price >= 0 else 0

print([get_price(i) for i in original_prices])
#12
words = ['Я', 'изучаю', 'Python']
res = [letter for word in words for letter in word]
print(res)

words1 = ['Я', 'изучаю', 'Python']
res1 = []
for word in words1:
    for letter in word:
        res1.append(letter)
print(res1)
#13
matrix = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
flat = [num for row in matrix for num in row]
print(flat)
t = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(t)
#14
a = [x for x in range(10000)]
b = (x for x in range(10000))
print(type(a), type(b))
import sys
print(sys.getsizeof(a), sys.getsizeof(b))
#15
d = {}
for num in range(1,10):
    d[num] = num**2
print(d)
d2 = {num: num**2 for num in range(1, 10)}
print(d2)
let = 'wrvetnb3490rj230ijgnvocnмцьщуешитмц'
d3 = {i: ord(i) for i in let}
print(d3)
#16
def FB(x):
    return 'FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x
d = {i: FB(i) for i in range(int(input("Введите число: "))+ 1) if type(FB(i)) == str}
print(d)
#17
import calendar
year, month = tuple(map(int, input().split()))
print(*[(day, month, year) for day in range(1, calendar.monthrange(year, month)[1] + 1)])