class StockSpanner:

    def __init__(self):
        # Initialize an/multiple empty list to store stock prices and their corresponding spans
        self.stockPrices = []
        self.spans = []

    def next(self, price: int) -> int:
        # Approach 1: a single monotonic stack, time and space O(n)
        counter = 1
        # pop elements from the stack while the current price is greater than or equal to the top of the stack
        while self.stockPrices and self.stockPrices[-1][0] <= price:
            # accumulate count
            counter += self.stockPrices.pop()[1]
        # append the current price and its span to the stack
        self.stockPrices.append((price,counter))
        return counter



        # # Approach 2: 2 monotonic stacks
        # # initialize the span for the current price to 1 (itself)
        # span = 1
        # # store prices in a non-increasing order
        # # if the current new price is greater than or equal to the price at the top of the stack
        # # include the span of that day into the current span
        # while self.stockPrices and price >= self.stockPrices[-1]:
        #     # add span from the top of the stack
        #     span += self.spans.pop()
        #     # remove the price at the top of the stack
        #     self.stockPrices.pop()
        # # append the current price and its span
        # self.stockPrices.append(price)
        # self.spans.append(span)
        # return span



        # # Approach 3: TLE, pass 95/99, simple queue recording all previous stock prices, time O(n^2)
        # self.stockPrices.append(price)
        # output = 1
        # for i in range(len(self.stockPrices)-2, -1, -1):
        #     if self.stockPrices[i] > price:
        #         break
        #     output +=1
        # return output
                


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)