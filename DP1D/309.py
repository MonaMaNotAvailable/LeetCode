class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Approach 1: iterative 1d dp, time & space O(n)
        noStock = [0] * n  # max profit on day i if we do not hold any stock
        holdStock = [0] * n  # max profit on day i if we hold stock
        cooldown = [0] * n  # max profit on day i if we are in cooldown
        holdStock[0] = -prices[0]  # If we buy on day 0
        
        for i in range(1, n):
            # either we didn't hold stock on day i-1, or we are coming from cooldown on day i-1
            noStock[i] = max(noStock[i - 1], cooldown[i - 1])
            # either we held stock on day i-1, or we bought stock today
            holdStock[i] = max(holdStock[i - 1], noStock[i - 1] - prices[i])
            # sold stock on day i-1, the profit is from selling stock on day i-1
            cooldown[i] = holdStock[i - 1] + prices[i]
        # not holding any stock (noStock[-1]) or in cooldown (cooldown[-1])
        return max(noStock[-1], cooldown[-1])



        # # Approach 2: recursion with memoization, time & space O(n)
        # @cache
        # def dp(i: int, state: int) -> int:
        #     # base case: if we have iterated through all days
        #     if i == n:
        #         return 0
        #     # initialize the result for this state
        #     ans = dp(i + 1, state)  # skip the current day
        #     if state == 0:  # not holding any stock
        #         ans = max(ans, dp(i + 1, 1) - prices[i])  # buy stock
        #     elif state == 1:  # holding a stock
        #         ans = max(ans, dp(i + 1, 2) + prices[i])  # sell stock
        #     elif state == 2:  # in cooldown
        #         ans = max(ans, dp(i + 1, 0))  # cool down
        #     return ans
        
        # # start from day 0 without holding any stock
        # return dp(0, 0)