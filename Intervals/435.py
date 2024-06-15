class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach 1: sort & record non-overlapping intervals (greedy), both approaches have time O(nlogn), space O(n)

        # sort the intervals based on their end times
        # pick the interval that ends the earliest and thus leaves the maximum room for future intervals
        intervals.sort(key=lambda x: x[1])
        # initialize the end time of the first interval and the count of non-overlapping intervals
        end = intervals[0][1]
        count = 1

        for i in range(1, len(intervals)):
            # if the start time of the current interval is not overlapping with the end time of the last non-overlapping interval
            if intervals[i][0] >= end:
                # update the end time to the end time of the current interval
                # always considering the next interval that has the least chance of overlapping with future intervals
                end = intervals[i][1]
                # increment the count of non-overlapping intervals
                count += 1

        return len(intervals) - count




        # # Approach 2: sort & merge, slower due to more conditional checks and list modifications
        # # sort the intervals based on their start times
        # intervals.sort(key=lambda x: x[0])

        # # keep track of merged intervals
        # merged_intervals = []
        # # counter for the number of removed intervals
        # result = 0
        
        # for interval in intervals:
        #     # if merged_intervals is empty or there is no overlap with the last merged interval
        #     if not merged_intervals or merged_intervals[-1][1] <= interval[0]:
        #         merged_intervals.append(interval)  # add the current interval to merged_intervals
        #     else:
        #         # there is an overlap, so we need to remove one interval
        #         result += 1
        #         # to maximize the chances of future merges, keep the interval with the smaller end time
        #         if merged_intervals[-1][1] > interval[1]:
        #             merged_intervals[-1] = interval  # replace the last interval in merged_intervals
        
        # return result  