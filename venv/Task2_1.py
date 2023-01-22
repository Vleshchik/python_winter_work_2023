n = int(input("Введите число: "))
if n > 0:
    for i in range(1, n+1):
        print(i, '*', n, '=', i * n)
elif n < 0:
    z = n * -1
    for i in range(1, z+1):
        print(i, '*', n, '=', i * n)
else:
    print("Результат умножения любого числа на 0 равен 0")