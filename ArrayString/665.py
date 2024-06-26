class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0  # count the number of changes
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if count == 1:
                    return False
                count += 1
                # # Approach 1: choose the modification that minimizes further violations down the array
                # # check if modifying nums[i-1] or nums[i] can fix the issue
                # # if we are at the beginning of the array, or if modify nums[i - 1] to nums[i] will still maintain the non-decreasing order up to nums[i - 2]
                # if i - 2 < 0 or nums[i] >= nums[i - 2]:
                #     nums[i - 1] = nums[i] # ensure that the change is less likely to cause a new violation
                # else:
                #     nums[i] = nums[i - 1] # ensure the current segment of the array becomes non-decreasing

                # Approach 2: nums[i - 1] remains unmodified unless absolutely necessary, time O(n), space O(1)
                # either we are at the start of the array
                # or modifying nums[i - 1] to nums[i] would not fix the non-decreasing property
                # modify nums[i] instead
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True



        # # Approach 3: use diff to analyze structure, time O(n), space O(n)
        # # if the array has one or two elements, it is already non-decreasing
        # if len(nums) == 1 or len(nums) == 2: 
        #     return True
        
        # count = 0  # to count the number of violations
        # diff = []  # to store the differences between consecutive elements
        
        # # iterate through the array to count violations and store differences
        # for i in range(len(nums) - 1):
        #     diff.append(nums[i + 1] - nums[i])  # store the difference
        #     if nums[i] > nums[i + 1]:  # if there is a violation
        #         count += 1
        #         if count > 1:  # if more than one violation, return False
        #             return False
        
        # # if the array has more than two differences, check further
        # if len(diff) > 2:
        #     for j in range(len(diff) - 1):
        #         # check if the sum of adjacent differences is negative and within bounds
        #         if ((diff[j + 1] + diff[j]) < 0) and (j < len(diff) - 2):
        #             # check if the next pair of differences also sum to a negative value
        #             if (diff[j + 2] + diff[j + 1]) < 0: 
        #                 return False
        # return True