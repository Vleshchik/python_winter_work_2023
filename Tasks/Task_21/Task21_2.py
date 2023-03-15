
matrix = [[1, 4, 2, 2],[1, 1, 2, 1],[4, 1, 3, 4],[1, 1, 4, 1]]
for i in matrix:
    print(i)
def minPathSum(matrix):
    res = 0
    if matrix:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = matrix[0][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = matrix[i][j]
                dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])

        res = dp[-1][-1]
    return res
print(minPathSum(matrix))