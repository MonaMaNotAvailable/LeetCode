class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(nums)-1

        # Approach 1: avoiding out-of-bound errors, minimizes the number of checks within the loop
        # loop until the pointers converge
        while leftPtr < rightPtr:
            # get the middle index to avoid overflow
            midPtr = leftPtr + (rightPtr - leftPtr) // 2
            # the peak element must be in the right half
            if nums[midPtr] < nums[midPtr + 1]:
                leftPtr = midPtr + 1
            # the peak element is in the left half (midPtr can be the peak)
            else:
                rightPtr = midPtr

            # # Approach 2: Binary search O(log n) and check valid midpoint explicitly
            # midPtr = leftPtr + (rightPtr-leftPtr)//2
            # # check if the middle element is greater than both its neighbors
            # # !!!potential issues at the boundaries
            # if nums[midPtr-1] < nums[midPtr] > nums[midPtr+1]:
            #     return midPtr
            # # the peak element must be in the right half
            # elif nums[midPtr] < nums[midPtr+1]:
            #     leftPtr = midPtr+1
            # # the peak element is in the left half
            # else:
            #     rightPtr = midPtr
        
        return leftPtr