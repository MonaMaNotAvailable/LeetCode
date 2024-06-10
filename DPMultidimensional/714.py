class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Approach 1: 2 variables to store the maximum profit
        buy = float('-inf') # maximum profit if we bought a stock so far
        sell = 0  # maximum profit if we sold a stock so far

        for price in prices:
            # update the buy state: either keep the previous buy or buy today with current sell profit
            buy = max(buy, sell - price)
            # update the sell state: either keep the previous sell or sell today with current buy profit minus fee
            sell = max(sell, buy + price - fee)
        return sell



        # # Approach 2: dp arrays to store the maximum profit
        # n = len(prices)
        # hold = [0] * n  # hold[i] is the max profit on day i with a stock in hand
        # cash = [0] * n  # cash[i] is the max profit on day i without a stock in hand
        # hold[0] = -prices[0]  # if we buy on the first day
        # cash[0] = 0  # if we do nothing on the first day

        # for i in range(1, n):
        #     # do nothing or buy
        #     hold[i] = max(hold[i-1], cash[i-1] - prices[i])
        #     # do nothing or sell
        #     cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
        # return cash[-1]



        # # Approach 3: recursion TLE: pass 19/44
        # def recursiveProfit(tradingDay:int, previousState:string, currentProfit:int) -> int:
        #     # base case
        #     if tradingDay == len(prices)-1:
        #         return currentProfit
        #     if previousState == "buy" or previousState == "keep":
        #         # sell
        #         ifSell = currentProfit + prices[tradingDay+1]-fee
        #         sellToday = recursiveProfit(tradingDay+1, "sell", ifSell)
        #         # keep
        #         keepToday = recursiveProfit(tradingDay+1, "keep", currentProfit)
        #         return max(sellToday, keepToday)
        #     else: # previousState = sell or nothing
        #         # buy
        #         ifBuy = currentProfit - prices[tradingDay+1]
        #         buyToday = recursiveProfit(tradingDay+1, "buy", ifBuy)
        #         # nothing
        #         doNothing = recursiveProfit(tradingDay+1, "nothing", currentProfit)
        #         return max(buyToday, doNothing)

        # firstDayBuy = recursiveProfit(0, "buy", -prices[0])
        # firstDayDoNothing = recursiveProfit(0, "nothing", 0)
        # return max(firstDayBuy, firstDayDoNothing)