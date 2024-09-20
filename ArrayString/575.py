class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Approach 1: set, both approaches have time & space O(1)
        differentTypes = set(candyType)
        return min(len(differentTypes),len(candyType)//2)

        # # Approach 2: dictionary
        # differentTypes = {}
        # for candy in candyType:
        #     if candy not in differentTypes:
        #         differentTypes[candy] = 0
        #     differentTypes[candy] += 1
        # return min(len(differentTypes),int(len(candyType)/2))