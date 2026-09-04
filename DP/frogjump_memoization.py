# Time: O(n)
# Space: O(n) DP + O(n) recursion stack

def frogjump(heights):
    n = len(heights)
    dp =[-1]*(n)

    def solve(i):
        if i == 0:
            return 0

        if dp[i] != -1:
            return dp[i]


        one_jump = solve(i-1) + abs(heights[i] - heights[i-1])
        two_jump = float('inf')

        if i > 1:
            two_jump = solve(i-2) + abs(heights[i] - heights[i-2])

        dp[i] = min(one_jump,two_jump)
        return dp[i]

    return solve(n-1)

heights = [3, 10, 3, 11, 3]

print(frogjump(heights))