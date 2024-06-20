class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Approach: 2d dp, time & space both O(kn)
        n = len(prices)
        # if k is greater than n//2, it is equivalent to unlimited transactions
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit
        # create a 2D list to store the maximum profit for up to k transactions on each day
        dp = [[0] * n for _ in range(k + 1)]
        # Iterate over the number of transactions (1 to k)
        for t in range(1, k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                # calculate the maximum profit on day i with t transactions
                dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
                # update max_diff to include the profit from the (t-1)th transaction
                max_diff = max(max_diff, dp[t-1][i] - prices[i])
        # the maximum profit with at most k transactions up to the last day
        return dp[k][n-1]