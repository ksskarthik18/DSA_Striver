#Time Complexity
# Time: O(n)
# Space: O(n) for DP + recursion stack

def fibonacci(n,dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci(n-1,dp) + fibonacci(n-2,dp)

    return dp[n]


n = 10
dp = [-1]*(n+1)
for i in range(n):
    print(fibonacci(i,dp),end=" ")