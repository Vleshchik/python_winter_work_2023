str1 = str(input('Введите первое предложение: ')) # АКВАРЕЛИСТ АНТИМОНИЯ АНАКОНДА ВЕРНОСТЬ ВЛАДЕНИЕ ЛЕПЕСТОК
str2 = str(input('Введите второе предложение: ')) # КАВАЛЕРИСТ АНТИНОМИЯ КАНОНАДА РЕВНОСТЬ ДАВЛЕНИЕ ТЕЛЕСКОП
marks = '''!@#$%^&*(){}[]\ |;:'",.<>/?_-1234567890+='''
for x in str1:
    if x in marks:
        str1 = str1.replace(x, "")
print(str1)
for x in str2:
    if x in marks:
        str2 = str2.replace(x, "")
print(str2)
dct = {}
if len(str1) == len(str2):
    for i in str1:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1
    print(dct)
    for i in str2:
        if i not in dct:
            print(False)
            break
        else:
            dct[i] -= 1
    print(dct)
else:
    print(False)
values = dct.values()
if min(values) == 0 and max(values) == 0:
    print(True)
else:
    print(False)