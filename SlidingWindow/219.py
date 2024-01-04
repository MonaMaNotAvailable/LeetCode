class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Approach1: maintain a set and record index
        index_dict = {}
        for i, n in enumerate(nums):
            # print(index_dict)
            if n in index_dict and i - index_dict[n] <= k:
                return True
            index_dict[n] = i

        return False



        #Approach2:  #maintain a queue
        # queue = nums[:k+1]
        # if len(queue) != len(set(queue)):
        #     return True
        # #slide through the nums with window size k
        # for i in range(k+1, len(nums)):
        #     queue.pop(0)
        #     if nums[i] in queue:
        #         return True
        #     else:
        #         queue.append(nums[i])
        
        # return False    