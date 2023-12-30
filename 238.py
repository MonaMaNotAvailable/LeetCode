class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Approach 1: Prefix and suffix, the fastest O(N)
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return sol

        #Approach 2: Prefix and suffix without division, faster 2*O(N)
        # count = len(nums)
        # output = [1]*count

        # #1 1 2 6
        # for i in range(1,count):
        #     output[i] = output[i-1]*nums[i-1]

        # #24 12 4 1
        # temp = 1
        # for j in range(count-2,-1,-1):
        #     output[j] *= temp*nums[j+1]
        #     temp *= nums[j+1]
        
        # #24 12 8 6
        # return output



        #Approach 3: 2*O(N) but used division
        # countZero = 0
        # product = 1
        # #go through all nums to find the ultimate product
        # for n in nums:
        #     if n == 0:
        #         countZero+=1
        #     else:
        #         product *= n

        # #no 0
        # if countZero == 0:
        #     for i in range(len(nums)):
        #         #divide by each integer
        #         nums[i]=int(product/nums[i])
        # #one 0
        # elif countZero == 1:
        #     i = nums.index(0)
        #     nums = [0]*len(nums)
        #     nums[i] = product
        # #>one 0s
        # else:
        #     nums = [0]*len(nums)
        
        # return nums