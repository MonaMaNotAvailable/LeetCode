class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: greedy, time O(n), space O(1)
        # initialize the maximum profit to 0
        curMax = 0
        # iterate over the prices starting from the second element
        for i in range(1, len(prices)):
            # calculate the profit if we bought at prices[i-1] and sold at prices[i]
            profit = prices[i] - prices[i-1]
            # multiple transactions are allowed, we add any positive profit to curMax 
            # equivalent to summing all positive differences
            if profit > 0:
                curMax += profit
        # total maximum profit
        return curMax



        # # Appraoch 2: top down dp / recursion, 2n state evaluations but still time O(n), space O(n)
        # n = len(prices)
        
        # @cache
        # def dp(i: int, hold: bool) -> int:
        #     # base case: if we have iterated through all days
        #     if i == n:
        #         return 0
        #     # initialize the result for this state
        #     ans = dp(i + 1, hold)  # skip the current day
        #     # sell if we are holding a stock
        #     if hold:
        #         ans = max(ans, prices[i] + dp(i + 1, False))
        #     # buy if we are not holding a stock
        #     else:
        #         ans = max(ans, dp(i + 1, True) - prices[i])
        #     return ans
        # # start from day 0 without holding any stock
        # return dp(0, False)