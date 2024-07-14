class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Approach 1: prefix sum with sliding window, time O(n), space O(n)
        # initialize the sum of elements and a dictionary to store the prefix sums
        iSum = 0
        pSum = {}  # v: minimum prefix sum with end=v
        iMax = -inf  # a very large negative number to handle no valid subarray case
        # iterate through each value in nums
        for v in nums:
            # update the sum with the current value
            iSum += v
            # check if (v - k) exists in the prefix sum dictionary
            if v - k in pSum:
                # update the maximum subarray sum if the condition is met
                iMax = max(iMax, iSum - pSum[v - k] + v - k)
            # check if (v + k) exists in the prefix sum dictionary
            if v + k in pSum:
                # update the maximum subarray sum if the condition is met
                iMax = max(iMax, iSum - pSum[v + k] + v + k)
            # update the prefix sum dictionary with the current value
            # only update if the value is not in the dictionary or the current sum is smaller
            if v not in pSum or pSum[v] > iSum:
                pSum[v] = iSum
        # check if iMax was updated from the initial large negative number
        # return 0 if no valid subarray was found
        return 0 if iMax == -inf else iMax



        # # Approach 2: TLE, pass 767/782, brute-force, time O(n^3), space O(1)
        # currentMax = -math.inf
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if abs(nums[j]-nums[i])==k:
        #             currentMax = max(currentMax, sum(nums[i:j+1]))
        # return currentMax if currentMax != -math.inf else 0