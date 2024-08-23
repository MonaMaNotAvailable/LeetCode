class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # Approach 1: sorting & per level calculation
        # time O(nlogn) where n = len(inventory), space O(1)
        # sort the inventory in descending order so we can process the highest values first
        inventory.sort(reverse=True)
        # append 0 to the end to handle the last group of items efficiently
        inventory.append(0)
        output = 0
        mod = 10**9 + 7  # modulus value to avoid overflow and meet problem constraints
        k = 1  # the number of balls with the current maximum value
        # iterate over the sorted inventory
        for i in range(len(inventory) - 1):
            # check if the current value is greater than the next value
            if inventory[i] > inventory[i + 1]:
                # calculate the total number of balls we can sell at this level
                sell = min(orders, k * (inventory[i] - inventory[i + 1]))
                # full represents the number of complete levels we can sell
                full, remainder = divmod(sell, k)
                # calculate and add profit from selling full levels
                output += k * (full * (inventory[i] + inventory[i] - full + 1)) // 2
                output %= mod  # apply modulus to keep the result within bounds
                # add profit from the remaining balls that don't complete a full level
                output += remainder * (inventory[i] - full)
                output %= mod  # apply modulus again
                # decrease the number of remaining orders
                orders -= sell
                # if all orders are fulfilled, break out of the loop
                if orders == 0:
                    break
            # increment k to include the next group of items with the current value
            k += 1
        # return the total profit after processing all orders
        return output



        # # Approach 2: max-heap, TLE, too many heap operations and orders reduce by 1 in each iteration
        # # time O(mlogn) where m = len(orders), space O(n)
        # negative = []
        # heapq.heapify(negative)
        # for num in inventory:
        #     heapq.heappush(negative, -num)
        
        # output = 0
        # while orders > 0:
        #     temp = heapq.heappop(negative)
        #     output += -temp
        #     heapq.heappush(negative, temp+1)
        #     orders -= 1

        # return output%(pow(10, 9)+7)