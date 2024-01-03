class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        #Approach 1: using default Counter
        cnt = Counter(arr)
        temp = cnt.values()
        return len(temp) == len(set(temp))



        #Approach 2: using dictionary
        # occur = {}

        # for i in arr:
        #     if i in occur:
        #         occur[i]+=1
        #     else:
        #         occur[i]=1
        
        # return len(occur.values()) == len(set(occur.values()))