dct = {}
s = list(input().split())
w_1 = s[0]
w_2 = s[1]
if len(w_1) == len(w_2):
    for i in w_1:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1
    print(dct)
    for i in w_2:
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

# сравнить минимальное и максимальное значение(values) словаря и если они равны 0 то анаграмма
