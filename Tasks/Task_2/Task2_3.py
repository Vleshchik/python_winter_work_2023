n = int(input('Введите число: '))
z = 1
if n == 0:
    print('Факториал числа', n, 'составляет:', z)
else:
    for i in range(1, n+1):
        z = z * i
    print('Факториал числа', n, 'составляет:', z)