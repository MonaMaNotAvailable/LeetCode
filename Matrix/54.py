class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Approach 1: directional traversal
        # both apprroaches have time & space O(m*n)
        # determine the number of rows (m) and columns (n)
        m, n = len(matrix), len(matrix[0])
        # calculate the total number of elements to traverse
        count = m * n
        # set initial direction to 1 (rightward)
        direction = 1
        # initialize starting positions for row (i) and column (j)
        i, j = 0, -1
        # initialize the result list to store the spiral order
        result = []
        # loop until the result list contains all elements
        while len(result) != count:
            # traverse horizontally (left to right or right to left)
            for _ in range(n):
                j += direction  # move in the current horizontal direction
                result.append(matrix[i][j])  # add the current element to result
            # decrement the number of rows to traverse
            m -= 1
            # traverse vertically (top to bottom or bottom to top)
            for _ in range(m):
                i += direction  # move in the current vertical direction
                result.append(matrix[i][j])  # add the current element to result
            # decrement the number of columns to traverse
            n -= 1
            # reverse the direction for the next loop
            direction *= -1
        return result



        # # Approach 2: boundary traversal
        # # initialize the boundaries for rows and columns
        # rowLowerBound = 0
        # rowUpperBound = len(matrix)
        # colLowerBound = 0
        # colUpperBound = len(matrix[0])
        # output = []
        # # loop until the bounds overlap
        # while rowLowerBound < rowUpperBound and colLowerBound < colUpperBound:
        #     # traverse from left to right
        #     for i in range(colLowerBound, colUpperBound):
        #         output.append(matrix[rowLowerBound][i])
        #     rowLowerBound += 1  # move the lower row bound up
        #     # traverse from top to bottom
        #     for j in range(rowLowerBound, rowUpperBound):
        #         output.append(matrix[j][colUpperBound-1])
        #     colUpperBound -= 1  # move the upper column bound left
        #     # check if there are remaining rows to traverse
        #     if rowLowerBound < rowUpperBound:
        #         # traverse from right to left
        #         for k in range(colUpperBound-1, colLowerBound-1, -1):
        #             output.append(matrix[rowUpperBound-1][k])
        #         rowUpperBound -= 1  # move the upper row bound down
        #     # check if there are remaining columns to traverse
        #     if colLowerBound < colUpperBound:
        #         # traverse from bottom to top
        #         for l in range(rowUpperBound-1, rowLowerBound-1, -1):
        #             output.append(matrix[l][colLowerBound])
        #         colLowerBound += 1  # move the lower column bound right
        # return output