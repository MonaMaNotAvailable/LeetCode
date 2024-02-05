class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = []

        #find all zeros index
        for i in range(n):
            if nums[i]==0:
                zeros.append(i)

        m = len(zeros)
        ans = 0

        #Edge case of no 1 or only one 1
        if m == 0 or m == 1:
            return n-1
        else: #defaut is start to the second zero
            ans = zeros[1]-1

        for l in range(2, m): #compare to substrings between zeros
            temp = zeros[l]-zeros[l-2]-2
            ans = max(ans, temp)
        
        #compare to the substring from the last second to the end 
        ans = max(ans, n-zeros[m-2]-2)
        return ans

        #Approach 1: TLE
        # s = sum(nums)
        # l = len(nums)
        # if s == l:
        #     return s-1
        # elif s == 1:
        #     return 1
        # #find sum of substrings
        # for i in range(l, 1, -1):
        #     for j in range(0, l-i+1):
        #         # print(i, j)
        #         # print(nums[j:j+i])
        #         temp = sum(nums[j:j+i])
        #         # print(temp)
        #         if temp == i:
        #             print("All ones")
        #             return temp-1
        #         elif temp == i-1:
        #             print("One zero")
        #             return temp
        #         elif temp == 0:
        #             return 0
        return 1