# Time: O(n)
# Space: O(n) DP + recursion stack.
def climbing_stairs(n,dp):
    if n <= 2:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = climbing_stairs(n-1,dp) + climbing_stairs(n-2,dp)

    return dp[n]

n = 4
dp = [-1]*(n+1)

print(climbing_stairs(n,dp))