class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Approach 1: transpose and reverse
        n = len(matrix)
        # transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # reverse each row
            matrix[i].reverse()



        # # Approach 2: rotating the outer-most layer
        # n = len(matrix)
        # left = 0
        # right = n - 1
        # while left < right:
        #     for i in range(right - left):
        #         # save the top element
        #         top = matrix[left][left + i]
        #         # move left element to top
        #         matrix[left][left + i] = matrix[right - i][left]
        #         # move bottom element to left
        #         matrix[right - i][left] = matrix[right][right - i]
        #         # move right element to bottom
        #         matrix[right][right - i] = matrix[left + i][right]
        #         # move top element to right
        #         matrix[left + i][right] = top
        #     # move towards inner layer
        #     left += 1
        #     right -= 1