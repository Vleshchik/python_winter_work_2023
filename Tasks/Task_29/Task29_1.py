def find(l):
    tes = set(l)
    l2 = []
    for i in tes:
        n = l.count(i)
        if n == 1:
            l2.append(i)
    if len(l2) == 1:
        return print(l2[0])
    else:
        return print('В предложенном списке такого числа нет')



find([1,1,1,1,1,1,1,1,1,1,1])
find([1,1,1,1,2,1,1,1,1,1,1])
find([1,1,1,1,11,1,1,1,20])
find([1,1,199,1,1,1,1,1,1,1,1])
find([1,15,1,1,1,1,1,1,1,1,1])
find([1,1,10,1,1,1,1,1,1,10,1])
