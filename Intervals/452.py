class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # key: holds the smallest end point of all overlapping intervals to guarantee the minimal number of arrows
        # time O(nlogn) space O(n)

        # Approach 1: sort by the end interval
        points.sort(key= lambda x:x[1])
        end = points[0][1]
        count = 1
        # print(points)

        for i in range(1, len(points)):
            # not overlap, need extra arrow
            if points[i][0] > end:
                count+=1
                end = points[i][1]
        return count



        # # Approach 2: sort by the start value
        # points.sort(key=lambda x: x[0])
        # end = points[0][1]
        # count = 1

        # for i in range(1, len(points)):
        #     # if the start of the current balloon is after the end of the last burst balloon
        #     if points[i][0] > end:
        #         count += 1
        #         end = points[i][1]  # update end to the end of the current balloon
        #     else: #without the else & taking min(), only pass 22/50 because it's not minimizing the number of arrows
        #         end = min(end, points[i][1])  # update end to the minimum end of overlapping intervals
        # return count