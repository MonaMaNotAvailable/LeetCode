class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Approach 1: monotonic stack, time O(n), both space O(n)
        n = len(temperatures)
        output = [0] * n
        stack = []  # store indices of temperatures array

        for i in range(n):
            # while the stack is not empty and the current temp is greater than the tempe at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                output[prev_index] = i - prev_index
            # push the current index onto the stack
            stack.append(i)
        
        return output



        # # Appraoch 2: brute-force, TLE, pass 39/48, time O(n^2)
        # globalMax = max(temperatures)
        # n = len(temperatures)
        # output = []

        # for i in range(n):
        #     wait = 0
        #     # flag to handle the case that no future day is greater
        #     possible = False
        #     for j in range(i+1, n):
        #         wait += 1
        #         if temperatures[j] > temperatures[i]:
        #             possible = True
        #             break
        #         elif temperatures[i] == globalMax:
        #             break
        #     if possible:
        #         output.append(wait)
        #     else:
        #         output.append(0)
        # return output