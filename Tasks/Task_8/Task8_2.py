n = int(input("Введите количество списков: "))
a = []
for i in range(n):
    m = int(input("Введите количество чисел в списке: "))
    b = []
    for j in range(m):
        x = int(input(f'Введите {(j + 1)} число: '))
        b.append(x)
    a.insert(i, b)
for i in range(len(a)):
    a[i] = sorted(a[i], reverse= True)
print(sorted(a, key = lambda x: len(str(x))))