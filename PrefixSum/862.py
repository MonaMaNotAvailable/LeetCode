class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Approach 1: prefix-sum with deque, time O(n), space O(n)
        n = len(nums)
        prefixSum = [0] * (n + 1)  # prefixSum[i] is the sum of nums[0] + ... + nums[i-1]
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        # deque to store the indices of prefixSum
        dq = deque()
        minLength = float('inf')
        for i in range(n + 1):
            # check if the current prefix sum minus the smallest prefix sum seen so far is >= k
            while dq and prefixSum[i] - prefixSum[dq[0]] >= k:
                minLength = min(minLength, i - dq.popleft())
            # maintain increasing order of prefix sums in the deque
            while dq and prefixSum[i] <= prefixSum[dq[-1]]:
                dq.pop()
            # add current index to deque
            dq.append(i)
        return minLength if minLength != float('inf') else -1



        # # Approach 2: TLE pass 82/98, brute-force, time O(n^2), space O(n)
        # # using deque to calculate all possible sum incrementally
        # if n == 1:
        #     # if there's only one element, check if it's greater than or equal to k
        #     if nums[0] >= k:
        #         return output
        #     else:
        #         return -1
        # # check if any single element is greater than or equal to k
        # for num in nums:
        #     if num >= k:
        #         return output
        # # initialize the deque with the input list
        # previousSums = deque(nums)
        # while output < n:
        #     # iterate through the remaining elements to build subarrays of increasing length
        #     for i in range(output, n):
        #         # pop the leftmost element and add the current element to form a new sum
        #         tempNum = previousSums.popleft()
        #         previousSums.append(tempNum + nums[i])
        #     # remove the first item in the deque from the previous round
        #     previousSums.popleft()
        #     output += 1
        #     # check if the maximum sum in the deque is greater than or equal to k
        #     if max(previousSums) >= k:
        #         return output
        # # if no valid subarray is found, return -1
        # return -1