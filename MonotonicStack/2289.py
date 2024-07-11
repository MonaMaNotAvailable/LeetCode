class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Approach 1: stack, time O(n), space O(n)
        stack = []
        maxSteps = 0
        for num in nums:
            steps = 0
            # pop elements from the stack while the current number is greater than or equal to the top of the stack
            while stack and stack[-1][0] <= num:
                steps = max(steps, stack.pop()[1])
            # if stack is not empty, increment steps
            if stack:
                steps += 1
            else:
                steps = 0
            # push the current number and its steps onto the stack
            stack.append((num, steps))
            # update maxSteps to be the maximum of maxSteps and the current steps
            maxSteps = max(maxSteps, steps)
        return maxSteps



        # # Approach 2: removing elements from the list in each iteration is inefficient
        # # TLE: pass 79/87, time O(n^2), space O(1)
        # count = 0
        # while True:
        #     removeIndex = []
        #     # find indices of elements to be removed in the current iteration
        #     for i in range(1, len(nums)):
        #         if nums[i-1] > nums[i]:
        #             removeIndex.append(i)
        #     # if there are elements to be removed, remove them and increment count
        #     if removeIndex:
        #         for index in removeIndex[::-1]:
        #             nums.pop(index)
        #         count += 1
        #     else:
        #         break
        # return count