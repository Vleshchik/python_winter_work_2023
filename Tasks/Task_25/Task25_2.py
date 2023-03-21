def abc(l):
    lst = []
    for i in range(len(l)-1):
        if l[i+1] - l[i] > 1:
            lst.append(l[i+1])
    return lst
l_n = [int(i) for i in input().split()] #1 5 6 7 9 10
print(abc(l_n))