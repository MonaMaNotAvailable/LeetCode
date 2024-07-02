class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Approach 1: prefix sum, time O(n) where n=len(ranges), space O(1)
        # initialize an array to track changes in coverage
        coverage = [0] * 52  # 52 to handle the range 0 to 51
        # mark the start and end of each range
        for r in ranges:
            coverage[r[0]] += 1
            coverage[r[1] + 1] -= 1
        # compute the prefix sum to get coverage at each point
        for i in range(1, 52):
            coverage[i] += coverage[i - 1]
        # check if all integers in the range [left, right] are covered
        for i in range(left, right + 1):
            if coverage[i] <= 0:
                return False
        return True



        # # Approach 2: sort the ranges based on the start value, time O(nlogn), space O(n) due to sorting
        # ranges.sort()
        # # iterate over each range
        # for start, end in ranges:
        #     if end < left:
        #         # skip ranges that end before 'left'
        #         continue
        #     if start > left:
        #         # if a range starts after 'left', there is a gap
        #         return False
        #     if end >= right:
        #         # if the current range covers up to or beyond 'right', return True
        #         return True
        #     # move the left boundary to one past the end of the current range
        #     left = end + 1
        # # if we exit the loop without covering the entire range, return False
        # return False



        # # Approach 3: brute-force, time O(n*m) where m=right-left+1, space O(1)
        # for i in range(left, right+1):
        #     covered = False
        #     for r in ranges:
        #         if i >= r[0] and i <= r[1]:
        #             covered = True
        #             break
        #     if not covered:
        #         return False
        # return True