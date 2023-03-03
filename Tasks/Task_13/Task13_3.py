lst = [str(x) for x in input().split()] # 1 2 3 4 5 7 9 135 110 11 22 33 100 101 109
def odd():
    for i in lst:
        n = int(i)
        if n % 2:
            yield n
        else:
            continue
gf = odd()
for i in gf:
    print(i, end= ' ')