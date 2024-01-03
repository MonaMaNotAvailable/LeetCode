class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 1: using XOR and reduce
        return reduce(lambda total, el: total ^ el, nums)



        # Approach 2: using XOR
        # uniqNum = 0
        # for idx in nums:
        #     # 4^1 == 101 == 5
        #     # 5^2 == 111 == 7
        #     # 7^1 == 110 == 6
        #     # 6^2 == 200 == 4
        #     uniqNum ^= idx
        # return uniqNum;  



        # Approach 3: using set, cosume more memory
        # return sum(set(nums))*2 - sum(nums)



        # Approach 4: maintain a list of nums have seen, slow
        # temp = []

        # for n in nums:
        #     if n not in temp:
        #         temp.append(n)
        #     else:
        #         temp.remove(n)
        
        # return temp[0]