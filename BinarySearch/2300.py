class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Approach 1: binary search
        # sort potions
        potions.sort(key=lambda x: x)
        output = []

        # binary search for each spell
        for spell in spells:
            goal = success/spell
            if potions[-1] < goal:
                output.append(0)
            else:
                lPtr = 0
                rPtr = len(potions)-1
                # find the smallest index lPtr such that potions[lPtr] is greater than or equal to goal
                while lPtr <= rPtr:
                    # calculate mid point
                    mid = lPtr + (rPtr-lPtr)//2
                    # continue in left
                    if potions[mid] >= goal:
                        rPtr = mid-1    
                    else: #continue in right
                        lPtr = mid+1
                # lPtr positioned at the first index where potions[lPtr] is greater than or equal to goal
                output.append(len(potions) - lPtr)
        return output



        # # Approach 2 (the fastest): using bisect_left: Locate the insertion point for x in a to maintain sorted order
        # potions.sort()
        # result = []
        # for a in spells:
        #     # calculates the smallest integer value of goal that ensures spell * potion >= success
        #     # integer division & round up using +a-1
        #     count = len(potions) - bisect_left(potions, (success + a - 1) // a)
        #     result.append(count)
        # return result