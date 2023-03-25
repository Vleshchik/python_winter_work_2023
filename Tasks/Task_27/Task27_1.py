n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = min(i, j, n - i - 1, n - j - 1) + 1
for row in matrix:
    print(" ".join(str(x) for x in row))