class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Approach 1: sliding window with 2 queues
        # Time Complexity: O(n), each element is processed at most twice (once added and once removed from deque).
        # Space Complexity: O(n), deques store indices of elements, and in the worst case, they can grow up to the size of the input array.
        minDeque = deque()  # deque to store indices of the minimum elements
        maxDeque = deque()  # deque to store indices of the maximum elements
        left = 0  # left boundary of the current window
        output = 0  # total count of valid subarrays
        for right in range(len(nums)):
            # update the minDeque to maintain increasing order
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)
            # update the maxDeque to maintain decreasing order
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            # check if the current window is valid
            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
                left += 1
                # remove indices out of the current window from minDeque
                if minDeque[0] < left:
                    minDeque.popleft()
                # remove indices out of the current window from maxDeque
                if maxDeque[0] < left:
                    maxDeque.popleft()
            # all subarrays ending at `right` and starting from `left` to `right` are valid
            output += right - left + 1
        return output



        # # Approach 2: brute-force TLE, pass 2110/2135
        # # Time Complexity: O(n^3), generating all subarrays and calculating min and max for each subarray.
        # # Space Complexity: O(n^2), in the worst case, we are storing multiple subarrays of increasing lengths. Each subarray slicing operation creates a new list, 
        # # and the total amount of space used by these lists can be quadratic in the size of the input array.
        # output = len(nums)  # initialize output with the number of single element subarrays
        # for i in range(2, len(nums)+1):  # start with subarray length 2 up to length of nums
        #     for j in range(len(nums)-i+1):  # iterate over all possible subarrays of length i
        #         tempList = nums[j:j+i]  # extract the subarray from index j to j+i
        #         if max(tempList) - min(tempList) <= 2:  # check if the subarray is valid
        #             output += 1  # increment the count of valid subarrays
        # return output