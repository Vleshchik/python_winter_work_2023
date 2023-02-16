def su():
    n = 0
    while True:
        n += 1
        yield n if n % 2 else -n
gf = su()
for i in gf:
    print(i, end = ' ')