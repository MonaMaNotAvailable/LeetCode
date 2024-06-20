class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: greedy, track the lowest prices for the first and second buys and the highest profits for the first and second sells
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0

        # iterate over each price in the list of prices
        for price in prices:
            # for the first buy, we want to find the minimum price to buy the stock
            buy1 = min(buy1, price)
            # for the first sell, we want to find the maximum profit possible by selling at the current price
            # after buying at the minimum price found so far (buy1)
            sell1 = max(sell1, price - buy1)
            
            # for the second buy, we consider the effective price after considering the profit from the first sell
            # we are buying the stock again after already having a profit from the first transaction
            buy2 = min(buy2, price - sell1)
            # for the second sell, we want to find the maximum profit possible by selling at the current price
            # after the second buy, which already accounts for the profit from the first transaction
            sell2 = max(sell2, price - buy2)
        # The maximum profit after at most two transactions is stored in sell2
        return sell2



        # # Approach 2: 2D dp with memoization, time O(n), space O(n)
        # n = len(prices)
        # # create a 2D list to store the maximum profit for up to 2 transactions on each day
        # dp = [[0] * n for _ in range(3)]
        
        # # iterate over the number of transactions (1 to 2)
        # for k in range(1, 3):
        #     # track the maximum difference of dp[k-1][j] - prices[j], avoids nested loops
        #     max_diff = -prices[0]
        #     # iterate over each day
        #     for i in range(1, n):
        #         # calculate the maximum profit on day i with k transactions
        #         # profit is the same as the profit on day i-1 with k transactions (dp[k][i-1])
        #         # or a transaction is made on day i (prices[i] + max_diff)
        #         dp[k][i] = max(dp[k][i-1], prices[i] + max_diff)
        #         # update max_diff to include the profit from the (k-1)th transaction
        #         # either the current value or the maximum profit with k-1 transactions up to day i minus the price of the stock on day i
        #         max_diff = max(max_diff, dp[k-1][i] - prices[i])
        
        # # the maximum profit with at most 2 transactions up to the last day
        # return dp[2][n-1]



        # # Approach 3: TLE, pass 201/214, top-down recursion, time O(2^n), space O(n)
        # def dp(index, holding, countTransactions) -> int:
        #     # base case
        #     if index == len(prices) or countTransactions == 2:
        #         return 0
        #     if holding: # sell it or do nothing
        #         return max(dp(index+1, 0, countTransactions+1)+prices[index], dp(index+1, 1, countTransactions))
        #     else: # buy it or do nothing
        #         return max(dp(index+1, 1, countTransactions)-prices[index], dp(index+1, 0, countTransactions))
        # return dp(0, 0, 0)