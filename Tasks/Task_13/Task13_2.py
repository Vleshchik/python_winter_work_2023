def num_pal():
    n = 0
    while True:
        n += 1
        s = list(str(n))
        if s == s[::-1]:
            yield n
        else:
            continue
gf = num_pal()
for i in gf:
    print(i, end = ' ')