class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If total is odd, it's impossible to split into two equal subsets
        if total % 2 != 0:
            return False

        # We just need one subset that sums to half
        target = total // 2

        # dp[s] = True means sum s is achievable using some subset of nums seen so far
        # Size target+1 to cover indices 0
        dp = [False] * (target + 1)
        # Base case: sum of 0 is always achievable (pick nothing)
        dp[0] = True

        for num in nums:
            # Traverse BACKWARDS to avoid using the same num twice in one pass. If we went forwards, an updated dp[s] could feed into dp[s + num] in the same iteration, effectively reusing num multiple times (unbounded knapsack).
            # Going backwards ensures each num is only counted once (0/1 knapsack).
            for s in range(target, num - 1, -1):
                # If sum (s - num) was achievable before, then sum s is now achievable
                # by adding num to that subset
                if dp[s - num]:
                    dp[s] = True

        # True if we can form a subset that sums exactly to half the total
        return dp[target]