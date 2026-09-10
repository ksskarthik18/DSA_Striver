def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    def rob_linear(arr):
        m = len(arr)
        prev2 = 0
        prev1 = 0

        for money in arr:
            curr = max(prev1,money+ prev2)
            prev2 = prev1
            prev1 = curr
        return prev1

    case1 = rob_linear(nums[1:])
    case2 = rob_linear(nums[:-1])

    return max(case1,case2)

nums = [2, 3, 2]
print(rob(nums))