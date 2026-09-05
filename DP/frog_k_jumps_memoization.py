def frogJump(heights,k):
    n = len(heights)

    dp = [-1]*n

    def solve(i):
        if i == 0:
            return 0

        if dp[i] != -1:
            return dp[i]

        min_energy = float('inf')

        for j in range(1,k+1):
            if i - j >= 0:
                energy = solve(i-j) + abs(heights[i] - heights[i-j])
                min_energy = min(energy,min_energy)

        dp[i] = min_energy
        return dp[i]

    return solve(n-1)

heights = [10, 5, 20, 0, 15]
k = 2

print(frogJump(heights, k))