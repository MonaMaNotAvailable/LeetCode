class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
	# both approaches have time & space O(n)
        # Approach 1: iterate through all intervals and update newInterval
        result = []
        for interval in intervals:
            # the new interval is after the range of the current interval
            # add the current interval to the result as there is no overlap
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval is before the range of the current interval
            # add the new interval to the result and update newInterval to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # there is an overlap, so merge the intervals by choosing the minimum start and maximum end
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        # add the last newInterval to the result
        result.append(newInterval)
        return result



        # # Approach 2: while loops to categorize intervals into 3 groups
        # result = []
        # i = 0
        # n = len(intervals)
        # # add all intervals that end before the new interval starts
        # while i < n and intervals[i][1] < newInterval[0]:
        #     result.append(intervals[i])
        #     i += 1 
        # # merge intervals that overlap with the new interval
        # while i < n and intervals[i][0] <= newInterval[1]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # result.append(newInterval)
        # # add all intervals that start after the new interval ends
        # while i < n:
        #     result.append(intervals[i])
        #     i += 1
        # return result