#[1, 4, 21, 3, 43]  [9, 81, 25] 1 4 21 3 43 12
s = [1, 4, 21, 3, 43, 15, 10, 494, 45]  #[11, 12, 13, 14, 15]
w = ''
s.sort(key= lambda x: (str(x)[0], -len(str(x))), reverse=True)
print(s)
for i in range(len(s)-1, 0, -1):
    for x in str(s[i-1]):
        for y in str(s[i]):
            if int(x) < int(y):
                s[i], s[i - 1] = s[i - 1], s[i]
                continue

print(s)
for i in s:
    w += str(i)
print(w)