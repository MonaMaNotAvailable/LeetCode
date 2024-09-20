class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Approach 1: bottom up dp (tabulation), both approaches have time O(amount*n) & space O(amount)
        # initialize an array to store the minimum number of coins for each amount
        # set each element to amount + 1, which is effectively infinity since it's more than any possible solution
        minCoins = [amount + 1] * (amount + 1)
        # base case: zero amount requires zero coins
        minCoins[0] = 0
        # iterate over all amounts from 1 to the target amount
        for i in range(1, amount + 1):
            # for each coin, try to update the minimum coins needed for the current amount i
            for c in coins:
                # check if it's possible to use the coin c (i.e., if i - c is non-negative)
                if i - c >= 0:
                    # update the minimum coins for amount i by considering using this coin
                    minCoins[i] = min(minCoins[i], 1 + minCoins[i - c])
        # if the value at the target amount is still amount + 1, it means it's not possible to form that amount
        return minCoins[-1] if minCoins[-1] != amount + 1 else -1



        # Approach 2: top down dp (memoization)
        def coinChangeInner(rem, cache):
            # if the remaining amount is negative, it's not possible to make the amount with the given coins
            if rem < 0:
                return math.inf
            # if the remaining amount is zero, no more coins are needed
            if rem == 0:                    
                return 0       
            # if the remaining amount is already computed and stored in the cache, return the cached result
            if rem in cache:
                return cache[rem]
            # recursively calculate the minimum number of coins needed by trying all coins
            # subtract each coin from the remaining amount and add 1 to account for the current coin being used
            # store the result in the cache to avoid recomputing it
            cache[rem] = min(coinChangeInner(rem - x, cache) + 1 for x in coins)                        
            # return the cached result for the current remaining amount
            return cache[rem]      
        # start the recursion with the full amount and an empty cache
        ans = coinChangeInner(amount, {})
        # if the result is infinity, it means no combination of coins can make the amount, so return -1
        # otherwise, return the calculated minimum number of coins
        return -1 if ans == math.inf else ans