class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        left = 0
        right = sum(nums)-nums[0]

        while i<len(nums):
            if left == right:
                return i
            else:
                left+=nums[i]
                if i+1<len(nums):
                    right-=nums[i+1] 
                i+=1
        return -1

        # #slower with slightly less storage (a sum vs. a changing rightSum)
        # total_sum = sum(nums)
        # left_sum = 0
        
        # for i, num in enumerate(nums):
        #     if left_sum == (total_sum - left_sum - num):
        #         return i
        #     left_sum += num
        
        # return -1

        # #slower with roughly same storage
        # leftSum, rightSum = 0, sum(nums)
        # for idx, ele in enumerate(nums):
        #     rightSum -= ele
        #     if leftSum == rightSum:
        #         return idx
        #     leftSum += ele
        # return -1