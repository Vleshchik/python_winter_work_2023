n = int(input())
a = [0] * n
for i in range(n):
    a[i] = [0] * n
c = 1
s = 0
for s in range(n // 2):
    j = n - s * 2 - 1
    for x in range(j):
        a[s][s + x] = c
        c += 1
    for y in range(j):
        a[s + y][n - 1 - s] = c
        c += 1
    for x in range(j):
        a[n - 1 - s][n - 1 - s - x] = c
        c += 1
    for y in range(j):
        a[n - 1 - s - y][s] = c
        c += 1
    s += 1
if n % 2 != 0:
    a[s][s] = c
for y in range(n):
    print(a[y])