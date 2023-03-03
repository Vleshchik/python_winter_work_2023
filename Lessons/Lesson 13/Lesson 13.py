def su():
    n = 0
    while True:
        n += 1
        for k in range(n):
            yield n
gf = su()
for i in range(10):
    print(next(gf), end = ' ')