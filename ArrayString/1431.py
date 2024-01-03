class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Approach 1: 2 liners
        greatest = max(candies)-extraCandies
        return [c>=greatest for c in candies]



        # Approach 2: reduction once to set limit & simplify if/else
        # greatest = max(candies)-extraCandies
        # output = []

        # for c in candies:
        #     output.append(c>=greatest) #fastest
            # # Equivalent to
            # # if c>=greatest:
            # #     output.append(True)
            # # else:
            # #     output.append(False)
        
        # return output



        # Approach 3: addtion for each kid 
        # greatest = max(candies)
        # output = []

        # for c in candies:
        #     if c+extraCandies>=greatest:
        #         output.append(True)
        #     else:
        #         output.append(False)
        
        # return output