x = str(input())
d = {}
key = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
for i in range(len(x)):
    if x[i] in key:
        d[i] = x[i]
a = []
n = int(input("Введите количество слов: "))
b = []
for i in range(n):
    w = str(input("Введите слово: "))
    a.append(w)
for i in range(len(a)):
    s = a[i]
    dic = {}
    for j in range(len(s)):
        if s[j] in key:
            dic[j] = s[j]
    if len(d) == len(dic):
        if d.keys() == dic.keys():
            b.append(s)
if len(b) > 0:
    print(f"Слова, похожие на {x} - это {b}.")
else:
    print(f"Слова, похожие на {x} отсутствуют.")




