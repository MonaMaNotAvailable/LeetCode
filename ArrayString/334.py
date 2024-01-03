class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Approach 1: find 2 mins
        # Time O(n)
        # Space O(1)
        currentMin = math.inf
        current2ndMin = math.inf
        # if not updating either, then the third must satisfy the increasing trend
        for n in nums:
            # if n <= currentMin:
            #     currentMin = n
            # elif n <= current2ndMin:
            #     current2ndMin = n
            # else: 
            #     return True

            # More optimized version
            if current2ndMin < n:
                return True
            if n <= currentMin:
                currentMin = n
            else:    
                current2ndMin = n        

        return False



        # Approach 2: find current max from right & current min from left
        # Time O(n)
        # Space O(n)
        # l = len(nums)
        # minLeft = [0]*l
        # minLeft[0] = nums[0]
        # for i in range(1,l-1):
        #     minLeft[i] = min(minLeft[i-1], nums[i])
        
        # maxRight = nums[-1]
        # for i in range(l-2, -1, -1):
        #     if minLeft[i] < nums[i] < maxRight:
        #         return True
        #     maxRight = max(maxRight, nums[i])
        
        # return False



        # Approach 3: find min & max, pass 64 / 83
        # currentMin = nums[0]
        # currentMax = nums[0]
        # iMin = 0
        # iMax = 0

        # for i in range(1,len(nums)):
        #     temp = nums[i]
        #     if temp < currentMin:
        #         currentMin = temp
        #         iMin = i
        #     elif temp > currentMax:
        #         currentMax = temp
        #         iMax = i
            
        #     if iMin < iMax-1:
        #         return True
        
        # return False