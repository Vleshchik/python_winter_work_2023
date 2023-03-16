s = []
for i in list(input().lower()):
    if i.isalpha():
        s.append(i) #Aa.bbc, cDd-cc
s = ''.join(s)
d = {}
l_pal = []
for i in s:
    l = []
    for j in range(len(s)):
        if s[j] == i:
            l.append(j)
    d.setdefault(i, l)
print(d)
for k, v in d.items():
    for i in range(len(v)-1):
        v.append(0)
        for j in range(i, len(v)-1):
            w = s[v[i]:v[j]+1]
            if w == w[::-1]:
                l_pal.append(len(w))
print(l_pal)
print(max(l_pal))
