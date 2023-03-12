import numpy as np
y = int(input()) #число столбцов в матрице
x = int(input()) #число строк в матрице
rang = [int(i) for i in input().split()] #диапазон чисел
matrix = np.random.randint(rang[0], rang[1], (x, y))
for i in matrix:
    print(i)
def short_path():
    i = 0
    j = 0
    sum = matrix[0, 0]
    path = []
    path.append(sum)
    while i != len(matrix) - 1 and j != len(matrix[i]) - 1:
        n1 = matrix[i + 1, j]
        n2 = matrix[i, j + 1]
        if n1 < n2:
            sum += n1
            i += 1
            path.append(n1)
        elif n1 > n2:
            sum += n2
            j += 1
            path.append(n2)
        else:
            if i + 2 <= len(matrix):
                if j + 2 <= len(matrix[i]):
                    n_1 = matrix[i + 2, j]
                    n_2 = matrix[i, j + 2]
                    if n_1 < n_2:
                        sum += n1
                        i += 1
                        path.append(n1)
                    else:
                        sum += n2
                        j += 1
                        path.append(n2)
                else:
                    sum += n1
                    i += 1
                    path.append(n1)
            else:
                sum += n2
                j += 1
                path.append(n2)
    else:
        if i == len(matrix):
            for z in range(j, len(matrix[i]) + 1):
                n = matrix[i, z]
                sum += n
                path.append(n)
            sum += matrix[-1,-1]
            path.append(matrix[-1,-1])
        else:
            for z in range(i + 1, len(matrix)):
                n = matrix[z, j]
                sum += n
                path.append(n)
    return path, sum

s_p, s = short_path()
print(f'Самый короткий маршрут: {s_p}')
print(f'Сумма чисел самого короткого маршрута: {s}')
