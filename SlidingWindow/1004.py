class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Approach1: account for the boundaries of the array
        zeros = []
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
        
        # If the number of zeros is less than or equal to k, flip them all.
        if len(zeros) <= k:
            return len(nums)
        
        # Add two sentinel values to simplify calculations.
        zeros = [-1] + zeros + [len(nums)]
        
        max_ones = 0
        # Slide the window of size k+1 over the zeros list.
        for i in range(len(zeros) - k - 1):
            # The number of 1s is the difference in indices minus 1.
            max_ones = max(max_ones, zeros[i + k + 1] - zeros[i] - 1)

        return max_ones

        # # Approach2: pass 53/55, can't handle [1,0,0,0]
        # #maintain a list of zeros
        # zeros = []

        # #iterate to find the index of all zeros
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zeros.append(i)
        
        # if k>=len(zeros):
        #     return len(nums)

        # zeros.insert(0,0)
        # zeros.append(len(nums))
        # print(zeros)

        # currentMax = 0
        # for j in range(1,len(zeros)-k):
        #     temp = zeros[j+k]-zeros[j-1]-1
        #     print(zeros[j-1], zeros[j+k])
        #     currentMax = max(temp, currentMax)
        #     print(currentMax)

        # return currentMax