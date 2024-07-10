class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # both approaches have time O(nlogn), space O(n)
        # sort by the start interval
        intervals.sort(key= lambda x:x[0])

        # Approach 1: avoid popping & pushing
        # initialize the result list with the first interval
        mergedIntervals = [intervals[0]]
        # iterate through the intervals starting from the second one
        for current in intervals[1:]:
            # get the last interval from the result to compare with the current interval
            lastMerged = mergedIntervals[-1]
            # check if the current interval overlaps with the last interval in the result
            if current[0] <= lastMerged[1]:
                # if they overlap, merge the intervals by updating the boundaries
                lastMerged[1] = max(lastMerged[1], current[1])
            else:
                # if they don't overlap, add the current interval to the result as a separate interval
                mergedIntervals.append(current)
        # Return the merged intervals
        return mergedIntervals



        # Approach 2: LIFO stack using pop()
        # # initialize the result list with the first interval
        # result = [intervals[0]]
        # # iterate through the intervals starting from the second one
        # for i in range(1, len(intervals)):
        #     # get the last interval from the result to compare with the current interval
        #     previousRange = result.pop()
        #     # check if the current interval overlaps with the last interval in the result
        #     if intervals[i][0] <= previousRange[1]:
        #         # If they overlap, merge the intervals by updating the boundaries
        #         lowerRange = min(previousRange[0], intervals[i][0])
        #         upperRange = max(previousRange[1], intervals[i][1])
        #         result.append([lowerRange, upperRange])
        #     else:
        #         # if they don't overlap, add the last interval back to the result
        #         result.append(previousRange)
        #         # add the current interval to the result as a separate interval
        #         result.append(intervals[i])
        # return result