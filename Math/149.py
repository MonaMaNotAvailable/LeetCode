class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Approach 1: dictionary uses floating-point number slope as keys
        # both approaches have time O(n^2), space O(n)
        # if there are 2 or fewer points, all points are on the same line
        if len(points) <= 2:
            return len(points)
        # function to find the slope between two points
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            # if the x-coordinates are the same, the line is vertical
            if x1 - x2 == 0:
                return math.inf
            # calculate and return the slope (dy/dx)
            return (y1 - y2) / (x1 - x2)
        ans = 1  # initialize the answer with the minimum number of points on a line
        # iterate through each point
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)  # dictionary to count occurrences of each slope
            # compare the current point with every other point
            for j, p2 in enumerate(points[i + 1:]):
                slope = find_slope(p1, p2)  # find the slope between the current point and another point
                slopes[slope] += 1  # increment the count of this slope
                # update the maximum points found on any line so far
                ans = max(slopes[slope], ans)
        # add 1 to include the initial point itself
        return ans + 1



        # # Approach 2: dictionary uses normalized integer slope as keys
        # # function to calculate gcd of two numbers
        # def gcd(a: int, b: int) -> int:
        #     while b:
        #         a, b = b, a % b
        #     return a
        # if not points:
        #     return 0
        # n = len(points)
        # # if there are 2 or fewer points, return the number of points
        # if n <= 2:
        #     return n
        # maxPoints = 1
        # # iterate through each point
        # for i in range(n):
        #     slopes = defaultdict(int)  # dictionary to store slopes and their counts
        #     verticals = 0  # counter for vertical lines
        #     # compare the current point with every other point
        #     for j in range(i + 1, n):
        #         dx = points[j][0] - points[i][0]  # difference in x-coordinates
        #         dy = points[j][1] - points[i][1]  # difference in y-coordinates
        #         # if dx is 0, the line is vertical
        #         if dx == 0:
        #             verticals += 1
        #         else:
        #             # reduce the slope (dy/dx) to its simplest form
        #             g = gcd(dx, dy)
        #             slope = (dy // g, dx // g)
        #             slopes[slope] += 1
        #     # maximum points on the current line considering vertical lines
        #     currentMax = verticals + 1
        #     for slope in slopes:
        #         currentMax = max(currentMax, slopes[slope] + 1)
        #     # update the global maximum points
        #     maxPoints = max(maxPoints, currentMax)
        # return maxPoints