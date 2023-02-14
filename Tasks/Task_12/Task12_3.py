lst = [str(x) for x in input().split(', ')] #1-2, 4-4, 3-6
def diapazon(lst):
    res = []
    for i in lst:
        print(i)
        n1 = int(i[0])
        n2 = int(i[2])
        while n1 <= n2:
            res.append(n1)
            n1 += 1
    return res
print(diapazon(lst))