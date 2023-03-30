
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matrix = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
print()
# Повернуть против часовой стрелки
for i in range(len(matrix)-1, -1, -1):
    for j in range(len(matrix)):
        print(matrix[j][i], end = ' ')
    print()
print()
# Повернуть по часовой стрелке
for i in range(len(matrix)):
    for j in range(len(matrix)-1, -1, -1):
        print(matrix[j][i], end = ' ')
    print()
print()
