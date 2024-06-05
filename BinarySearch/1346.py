class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Approach 1: O(NlogN) using binary search
        arr.sort()
        for i in range(len(arr)):
            product = arr[i]*2
            # left can't start from i+1 due to negative numbers
            left, right = 0,len(arr)-1
            while left <= right:
                mid = (left+right)//2
                # mid != i for handling 0
                if arr[mid]==product and mid != i:
                    return True
                elif arr[mid]<product:
                    left = mid+1
                else:
                    right = mid-1
        return False



        # # Approach 2: O(N) with set, the optimal solution
        # seen = set()
        # for num in arr:
        #     # if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
        #     # Python's set only contains integers in this context
        #     if num * 2 in seen or num / 2 in seen:
        #         return True
        #     seen.add(num)
        # return False



        # # Approach 3: O(N^2) with nested loop
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         if arr[j] == arr[i]/2 or arr[j] == arr[i]*2:
        #             return True
        # return False



        # # Approach 4: O(N^2) with set
        # while arr:
        #     num = arr.pop()
        #     tempSet = set(arr)
        #     if num/2 in tempSet or num*2 in tempSet:
        #         return True
        # return False



        # # Approach 5: O(N) with counter
        # s = collections.Counter(arr)
        # #check if there are more than one zeros
        # if(s[0]>1): 
        #     return True
    
        # for num in arr:
        #     if s[2*num] and num!=0:
        #         return True
        # return False