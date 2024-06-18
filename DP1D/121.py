class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: keep track of minPrice & maxProfit so far
        # time O(n) space O(1)
        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices[1:]:
            # Calculate the profit if we sell at the current price
            maxProfit = max(maxProfit, price - minPrice)
            # Update the minimum price encountered so far
            minPrice = min(price, minPrice)
        return maxProfit



        # # Approach 2: Kadane's Algorithm for maximum subarray problem
        # curDiff, curMax = 0, 0
        # for i in range(1, len(prices)):
        #     # calculate the difference between consecutive prices
        #     diff = prices[i] - prices[i-1]
        #     # find the maximum subarray sum
        #     curDiff = max(0, curDiff + diff)
        #     curMax = max(curDiff, curMax)
        # return curMax