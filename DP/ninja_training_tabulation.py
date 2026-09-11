#Time Complexity : O(n)
#Space Complexity : O(n)
def ninja_training(matrix):
    n = len(matrix)

    dp = [[0]*3 for _ in range(n)]

    dp[0][0] = matrix[0][0]
    dp[0][1] = matrix[0][1]
    dp[0][2] = matrix[0][2]

    for i in range(1,n):
        dp[i][0] = matrix[i][0] + max(dp[i-1][1],dp[i-1][2])

        dp[i][1] = matrix[i][1] + max(dp[i-1][0],dp[i-1][2])

        dp[i][2] = matrix[i][2] + max(dp[i-1][0],dp[i-1][1])

    return max(dp[n-1])

matrix = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]

print(ninja_training(matrix))