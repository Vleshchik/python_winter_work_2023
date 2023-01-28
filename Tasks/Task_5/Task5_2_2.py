import math
n = int(input())
a = []
a_c = []
for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        a.append(i)
        n //= i
if n != 1:
    a.append(n)
for i in a:
    if i not in a_c:
        a_c.append(i)
for i in range(len(a_c)):
    print(a_c[i], '-', a.count(a_c[i]))