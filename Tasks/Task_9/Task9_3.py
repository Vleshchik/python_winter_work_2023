f = open("test1.txt", "r", encoding="UTF-8")
text = str(f.readlines()).lower()
tes = set(text)
dic = {}.fromkeys(tes, 0)
for a in text:
    for i in a:
        dic[i] += 1
d = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
d = dict(list(d.items())[:10])
for k, v in d.items():
    print(k, '-', v)

