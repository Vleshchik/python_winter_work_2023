f = open("test1.txt", "r", encoding="UTF-8")
text = []
for line in f:
        line = line.strip().lower()
        text.append(line)
tes = set()
for i in text:
    for j in i:
        tes.add(j)
dic = {}.fromkeys(tes, 0)
for a in text:
    for i in a:
        if i in tes:
            dic[i] += 1
d = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
d = dict(list(d.items())[:10])
for k, v in d.items():
    print(k, '-', v)

