n = int(input("Введите количество элементов списка: "))
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
lst.sort()
print("Наименьшее число из списка: ", lst[0])