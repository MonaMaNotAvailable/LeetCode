class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        output1 = list(set1 - set2)
        output2 = list(set2 - set1)
        
        return [output1, output2]

        # Really slow...
        # find Union set(U) of nums1 and nums2
        # total = set(nums1+nums2)
        # print(total)

        # find set(U-nums1) and set(U-nums2)
        # output1 = set()
        # output2 = set()

        # for n in total:
        #     if n not in nums2:
        #         output1.add(n)
        #     elif n not in nums1:
        #         output2.add(n)
        
        # covert set to list
        # return [sorted(output1), sorted(output2)]
        