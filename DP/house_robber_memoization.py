# Time: O(n)
# Space: O(n) for DP + O(n) recursion stack.

def house_robber_memoization(nums):
    n = len(nums)
    dp = [-1]*n

    def solve(i):
        if i < 0:
            return 0
        if i == 0:
            return nums[0]

        if dp[i]!= -1:
            return dp[i]

        pick = nums[i] + solve(i-2)
        not_pick = solve(i-1)

        dp[i] = max(pick,not_pick)

        return dp[i]

    return solve(n-1)

nums=[2,7,9,3,1]
print(house_robber_memoization(nums))

        