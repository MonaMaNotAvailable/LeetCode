class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach1: More memory efficient
        curr, prev = 0,0
        for n in nums:
            curr, prev =  max(prev+n, curr), curr
        return curr

        # Approach2: Top down rolling window
        # # 0 1 2 3 4 5...
        # #0: 0
        # #1: 0 or 1
        # #2: 1 or 0+2
        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1])

        # output = [0]*len(nums)
        # output[0] = nums[0]
        # output[1] = max(nums[0],nums[1])
        # output[2] = max(output[0]+nums[2], output[1])
        # for i in range(3,len(nums)):
        #     output[i] = max(output[i-2]+nums[i], output[i-1])
        #     print(output)
        
        # return output[len(nums)-1]