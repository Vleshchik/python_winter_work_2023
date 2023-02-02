n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
a = []
for i in range(n):
    b = []
    for j in range(m):
        x = int(input())
        b.append(x)
    a.insert(i,b)
for y in range(n):
    print(a[y])
def srt(a):
    lst = []
    for i in range(n):
        b = a[i]
        for j in range(m):
            lst.append(b[j])
    x = len(lst) - 3
    lst = sorted(lst)[x:]
    return lst
print(srt(a))