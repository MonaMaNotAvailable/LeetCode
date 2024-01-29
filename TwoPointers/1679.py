class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #Approach 1: Delete immediately if no matching pair is found,
        # continuously shrinking the size of the counter(map)
        temp = Counter(nums)
        count = 0
        # create a list of keys to iterate over (to avoid RuntimeError)
        keys = list(temp.keys())

        for n in keys:
            if n in temp:
                pair = k-n
                if pair == n: #if same, add 1/2 pairs directly
                    count+=temp[n]//2
                else:
                    if pair in temp:
                        #if match, add the smaller count
                        minFreq = min(temp[n], temp[pair])
                        count+=minFreq
                        #delete the matching one because no others will match with it
                        del temp[pair]
                #delete current one because no others will match with it
                del temp[n]

        return count



        #Approach 2:  Use map
        # temp = Counter()
        # count = 0
        # for n in nums:
        #     current = k-n
        #     if n in temp.keys():
        #         count+=1
        #         if temp[n]==1:
        #             del temp[n]
        #         else:    
        #             temp[n]-=1
        #     else:
        #         temp[current]+=1
        # return count



        #Approach 3: Use list
        #TLE: 45/51 passed
        # temp = []
        # count = 0
        # for n in nums:
        #     current = k-n
        #     if n in temp:
        #         count+=1
        #         temp.remove(n)
        #     else:
        #         temp.append(current)
        # return count