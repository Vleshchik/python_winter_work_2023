#1
import re
text = 'fizz.123.buzz.456.fizzbuzz'
res1 = re.sub(r'\d+', r'#', text)
res2 = re.sub(r'[a-z]+', r'(*)', text)
print(res1)
print(res2)
#2
import re
def fullname(x):
    s = x.group()
    print(x.group(), x.start(), x.end())
    match s:
        case 'Коля': return 'Николай'
        case 'Миша': return 'Михаил'
text = 'Здравствуй, Коля! Привет, Миша!'
print(re.sub(r'\b\w{4}\b', fullname, text))
#3
import re
def airport(x):
    s = x.group()
    print(x.group(), x.start(), x.end())
    match s:
        case 'LED': return 'Пулково'
        case 'MSQ': return 'Минск'
        case 'SVO': return 'Шереметьево'
        case 'SVX': return 'Кольцово'
        case 'VNO': return 'Вильнюс'
text = 'Твой маршрут: LED - MSQ - VNO - MSQ - SVO - SVX'
print(re.sub(r'\b\w{3}\b', airport, text))
#4
import re
text = 'Лещик Вадим Дмитриевич'
print(re.sub(r'(Лещик) (Вадим) (Дмитриевич)', r'\2 \3 \1', text))
#5
import re
text = 'www.itmo.ru, www.tut.by, www.google.com, www.sverige.se'
print(re.findall(r'www\.(\w+)\.[ru|by|com]', text))
#6
import re
text = 'abracadabra'
res = re.finditer(r'a', text)
for i in res:
    print(i.group(), i.start(), i.end())
#7
import re
text = 'a. b, r!! a? c;;; ad. ab, ra'
def split(x):
    return print(re.split(r'[\.\,\;\!\?\s]+', text))
split(text)
#8
import re
text = 'у нас есть 2 книги по питону, 5 книг по джаве и 1 книга по windows'
def sqr(x):
    s = int(x.group())
    return str(s ** 2)
print(re.sub(r'\d+', lambda x: str(int(x.group()) ** 2), text))
#9
import re
x = 5
res = '|'.join(str(i) for i in range(x))
print(re.findall(fr'{res}', '112233445566'))
#10
def fu(f):
    return f
def hello():
    print('Hello')
fff = fu(hello)
fff()
hello()
fu(hello)()
#11
def sample(fu):
    def wrapper():
        print('Begin')
        fu() # мы обертываем функцию fu, не вмешиваясь в ее работу
        print('End')
    return wrapper
def say():
    print('Hello World!')
say = sample(say) # декорируем функцию
say() #вызываем декорированную функцию
#12
import time
def sample(fu):
    def wrapper():
        print('Begin', time.time())
        fu() # мы обертываем функцию fu, не вмешиваясь в ее работу
        time.sleep(5)
        print('End', time.time())
    return wrapper
def say():
    print('Hello World!')
say = sample(say) # декорируем функцию
say() #вызываем декорированную функцию
def bye():
    print('Goodbye, world')
bye = sample(bye)
bye()
#13
def uppercase_decorator(fu):
    def wrapper():
        original_r = fu()
        modified_r = original_r.upper()
        return modified_r
    return wrapper
@uppercase_decorator  # <- это то же самое, что и - text = uppercase_decorator(text)
def text():
    return 'Hello World!'
print(text())
#14
def lowercase_decorator(fu):
    def wrapper():
        original_r = fu()
        modified_r = original_r.lower()
        return modified_r
    return wrapper
@lowercase_decorator
def text():
    s = input()
    return s
print(text())
