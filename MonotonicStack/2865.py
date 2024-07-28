class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        # Approach 1: monotonic stack, time and space both O(n)
        n = len(heights)  # get the number of buildings
        left = [0] * n  # initialize left sums array
        right = [0] * n  # initialize right sums array
        stack = []  # initialize stack for calculating left sums
        for i in range(n):  # iterate through each building from left to right
            while stack and heights[stack[-1]] > heights[i]:  # pop from stack until finding a shorter building
                stack.pop()
            if stack:  # if stack is not empty, calculate left sum based on last building in stack
                left[i] = left[stack[-1]] + (i - stack[-1]) * heights[i]
            else:  # if stack is empty, all previous buildings are taller
                left[i] = (i + 1) * heights[i]
            stack.append(i)  # push current index to stack
        stack = []  # clear stack for right sums calculation
        for i in range(n-1, -1, -1):  # iterate through each building from right to left
            while stack and heights[stack[-1]] > heights[i]:  # pop from stack until finding a shorter building
                stack.pop()
            if stack:  # if stack is not empty, calculate right sum based on next building in stack
                right[i] = right[stack[-1]] + (stack[-1] - i) * heights[i]
            else:  # if stack is empty, all subsequent buildings are taller
                right[i] = (n - i) * heights[i]
            stack.append(i)  # push current index to stack
        result = 0  # initialize the result variable
        for i in range(n):  # iterate through each building to find the maximum sum
            result = max(result, left[i] + right[i] - heights[i])  # calculate sum and update result
        return result  # return the maximum sum found



        # # Approach 2: brute force, try all indices since the peak is not necessarily the maximum of the list
        # time O(n^2), space O(1)
        # # # identify the peak
        # # peak = max(heights)
        # result = 0
        # # # if multiple peaks
        # # indices = [i for i, x in enumerate(heights) if x == peak]
        # for peakIndex in range(len(heights)): #indices:
        #     output = heights[peakIndex] #peak
        #     # process left side
        #     currentMax = heights[peakIndex] #peak
        #     for i in range(peakIndex-1, -1, -1):
        #         if heights[i] < currentMax:
        #             currentMax = heights[i]
        #         output += currentMax
        #     # process right side
        #     currentMax = heights[peakIndex] #peak
        #     for j in range(peakIndex+1, len(heights)):
        #         if heights[j] < currentMax:
        #             currentMax = heights[j]
        #         output += currentMax
        #     result = max(result, output)
        # return result