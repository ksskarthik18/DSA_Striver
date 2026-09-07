#Time Complexity : O(N)
#Space Complexity : O(N)
def rob(nums):
    n = len(nums)

    dp = [0]*n

    dp[0] = nums[0]

    if n > 1:
        dp[1] = max(dp[0],dp[1])

    for i in range(2,n):
        pick = nums[i] + dp[i-2]
        not_pick = dp[i-1]

        dp[i] = max(pick,not_pick)

    return dp[n-1]
nums = [2, 7, 9, 3, 1]

print(rob(nums))