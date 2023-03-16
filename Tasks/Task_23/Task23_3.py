#[1, 4, 21, 3, 43]  [9, 81, 25] 1 4 21 3 43 12
s = [1, 4, 21, 3, 43, 15, 10, 45]  #[11, 12, 13, 14, 15]
w = ''
leng = max(sorted(s, key= lambda x: len(str(x))))
s.sort(key= lambda x: (str(x)[0], -len(str(x))), reverse=True)

for i_0 in range(len(s)-1, 0, -1):
    for i in range(len(s)-1, 0, -1):
        if str(s[i])[0] == str(s[i-1])[0]:

            if len(str(s[i - 1])) < len(str(s[i])):
                n = int(str(s[i])[1:])
                if s[i-1] < n:
                    s[i], s[i - 1] = s[i - 1], s[i]

            elif len(str(s[i - 1])) == len(str(s[i])):
                if s[i] > s[i - 1]:
                    s[i], s[i - 1] = s[i - 1], s[i]
for i in s:
    w += str(i)
print(w)