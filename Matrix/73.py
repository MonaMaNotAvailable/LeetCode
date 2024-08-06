class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)  
        n = len(matrix[0])  

        # approach 1: use the first row and first column to store the zero state for each row and column
        # time O(m*n), space O(1)
        firstRowZero = False
        firstColZero = False
        # use the first row and first column to mark zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0: # determine if the first row needs to be zeroed
                        firstRowZero = True
                    if j == 0: # determine if the first column needs to be zeroed
                        firstColZero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # zero out cells based on the markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # zero out the first row if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        # zero out the first column if needed
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0



        # # Approach 2: gather indexes first
        # # both approaches have time and space O(m*n)
        # idx = []  # list to store the positions of zeros
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:  # if an element is zero
        #             idx.append([i, j])  # record its position
        # for i, j in idx:
        #     matrix[i] = [0]*n  # set the entire row to zeros
        #     for x in range(m):
        #         matrix[x][j] = 0  # set the entire column to zeros



        # approach 3: set zeros along the way using set
        # visited = set()  # set to keep track of visited cells
        # for i in range(m):
        #     for j in range(n):
        #         currentCell = matrix[i][j]
        #         if currentCell == 0 and (i, j) not in visited:             
        #             for k in range(n): # set row
        #                 if matrix[i][k] != 0:
        #                     matrix[i][k] = 0
        #                     visited.add((i, k))  # add to visited set             
        #             for l in range(m): # set col
        #                 if matrix[l][j] != 0:
        #                     matrix[l][j] = 0
        #                     visited.add((l, j))  # add to visited set
        #             visited.add((i, j))  # add the original zero position to visited set