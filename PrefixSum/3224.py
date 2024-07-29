class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # Approach 1: prefix sum, time O(n+k), space O(k)
        n = len(nums)             
        changeCount = [0] * (k + 2)  # initialize the change count array with zeros
        changeCount[0] = n // 2  # the initial number of changes needed for zero difference
        for i in range(n // 2):
            left = nums[i]
            right = nums[n - i - 1]
            curDiff = abs(left - right)  # calculate the current difference between the pair
            maxDiff = max(left, right, k - left, k - right)  # calculate the maximum possible difference
            changeCount[curDiff] -= 1  # decrease the count for the current difference
            changeCount[curDiff + 1] += 1  # increase the count for the next difference
            changeCount[maxDiff + 1] += 1  # increase the count for the maximum difference
        curChanges = 0
        minChanges = n // 2  # initialize the minimum changes with half the length of the array
        for i in range(k + 1):
            curChanges += changeCount[i]  # accumulate the changes
            minChanges = min(minChanges, curChanges)  # update the minimum changes
        return minChanges  # return the minimum number of changes required



        # # Failed approach: pass 679/682, maxValue is not necessarily the fixed diff that is optimal
        # # time O(n^2), space O(n)
        # n = len(nums)
        # occurrencesMap = {}
        # maxValue = 0
        # # iterate over the first half of the list
        # for i in range(n // 2):
        #     diff = abs(nums[i] - nums[n - i - 1])  # calculate the absolute difference between symmetric elements
        #     if diff not in occurrencesMap:
        #         occurrencesMap[diff] = []
        #     occurrencesMap[diff].append((nums[i], nums[n - i - 1]))  # store the pairs in the occurrences map
        #     maxValue = max(maxValue, len(occurrencesMap[diff]))  # update maxValue with the maximum frequency of differences    
        # # print(occurrencesMap)
        # # print(maxValue)
        # fixedDiff = []
        # # find the differences that have the maximum frequency
        # for diff, pairs in occurrencesMap.items():
        #     if len(pairs) == maxValue:
        #         fixedDiff.append(diff)
        # # print(fixedDiff)
        # minChange = n // 2 - maxValue  # minimum changes required to make the most frequent difference
        # extraChange = minChange
        # # iterate over possible fixed differences to calculate extra changes required
        # for option in fixedDiff:
        #     temp = 0
        #     for diff, pairs in occurrencesMap.items():
        #         if diff != option:
        #             print(pairs)  # print pairs for debugging
        #             for pair in pairs:
        #                 # check if changing the pair to match the fixed difference exceeds the boundary conditions
        #                 if max(pair) + (option - diff) > k and min(pair) - (option - diff) < 0:
        #                     temp += 1
        #     extraChange = min(extraChange, temp)  # update extraChange with the minimum extra changes required
        # return minChange + extraChange  # return the total minimum changes required