import math
lst = list(map(int, input().split()))
def nok(lst):
    nok = lst[0]
    for i in range(len(lst) - 1):
        nok = math.lcm(nok, lst[i + 1])
    return nok
print(nok(lst))