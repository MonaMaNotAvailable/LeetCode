class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #maintain a monotonic decreasing stack
        stack = []
        curMin = nums[0]

        #finding the 2 in the 132 pattern
        for n in nums[1:]:
            #get rid of smaller ones in stack
            while stack and n >= stack[-1][0]:
                stack.pop()
            #check in range
            if stack and n > stack[-1][1]:
                return True

            #update min
            curMin = min(n,curMin)
            stack.append([n,curMin])
        
        return False


        #***************Failed previous attemps***************



        # n = len(nums)

        # if n<3:
        #     return False
        


        #Attemp 5: 79/103
        # gmax = max(nums)
        # imax = nums.index(gmax)
        # gmin = min(nums)
        # imin = nums.index(gmin)

        # for i in range(n-1, 0, -1):
        #     # print(i)
        #     # print(gmin , nums[i] , gmax)
        #     # print(imin , imax , i)
        #     if gmin < nums[i] < gmax and imin < i and imax < i:
        #         return True



        #Attemp 4: 84/103
        # gmax = max(nums)
        # imax = nums.index(gmax)
        # gmin = min(nums)
        # imin = nums.index(gmin)

        # for i in range(n-1, 0, -1):
        #     print(i)
        #     print(gmin , nums[i] , gmax)
        #     print(imin , imax , i)
        #     if gmin < nums[i] < gmax and imin < imax < i:
        #         return True



        #Attemp 3: 94/103 & TLE
        # for i in range(0, n - 2):
        #     for j in range(i + 1, n - 1):
        #         if nums[j]-nums[i]>=2:
        #             for k in range(j + 1, n):
        #                 if nums[i] < nums[k] < nums[j]:
        #                     return True



        #Attemp 2: 96/103
        # for i in range(0,n-2):
        #     print(nums[i])
        #     for j in range(i+1, n-1):
        #         print(nums[i], nums[j])
        #         if nums[j]-nums[i]<2:
        #             break
        #         else:
        #             for k in range(j+1, n):
        #                 print(nums[i], nums[j], nums[k])
        #                 if nums[k] > nums[i] and nums[k] < nums[j]:
        #                     return True



        #Attemp 1: 86/103
        # for i in range(1,n-2):
        #     print(nums[i], nums[i+1], nums[i-1])
        #     if nums[i] > nums[i+1] and nums[i+1]>nums[i-1]:
        #         return True
        
        # return False
        
        