class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        do not return anything, modify board in-place instead
        """
        # Approach 1: modify in-place, time O(mn), space O(1)
        # mark all cells that change from live (1) to dead as -1, 
        # this indicates that the cell was originally 1 but will change to 0
        # mark all cells that change from dead (0) to live as 2, 
        # this indicates that the cell was originally 0 but will change to 1
        m, n = len(board), len(board[0])  # get the dimensions of the board
        # directions array to check the 8 possible neighbors for each cell
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]] 
        
        # first pass: iterate through each cell to count live neighbors and mark changes
        for i in range(m):
            for j in range(n):
                livecount = 0  # initialize a counter to count live neighbors
                
                # check all 8 possible neighbors using the direction array
                for r, c in dirs:
                    nr, nc = i + r, j + c  # calculate the coordinates of the neighbor cell
                    # make sure the neighbor is within bounds and is a live cell (abs(b[nr][nc]) == 1)
                    # we use abs() because a cell could have been marked as -1 (originally live)
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:  
                        livecount += 1  # if the neighbor was originally alive, increment the live count
                
                # apply the rules based on the live neighbor count for the current cell
                if board[i][j] == 1:  # if the current cell is alive
                    if livecount < 2 or livecount > 3:  # it dies from under-population or over-population
                        board[i][j] = -1  # mark as -1 (originally alive but will become dead)
                else:  # if the current cell is dead
                    if livecount == 3:  # it becomes alive due to reproduction
                        board[i][j] = 2  # mark as 2 (originally dead but will become alive)
        
        # second pass: update the board based on the marked changes (-1 becomes 0, 2 becomes 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:    # if marked as 2 (dead to alive)
                    board[i][j] = 1      # change it to live (1)
                elif board[i][j] == -1:  # if marked as -1 (alive to dead)
                    board[i][j] = 0      # change it to dead (0)



        # # Approach 2: my approach, maintain a mask for flipping, time O(m*n), space O(m*n)
        # # get the number of rows and columns in the board
        # m = len(board)
        # n = len(board[0])
        # # create a mask (tempArray) to record which cells need to be flipped
        # tempArray = [[0 for _ in range(n)] for _ in range(m)]
        # # iterate through each cell in the board
        # for i in range(m):
        #     for j in range(n):
        #         # store the current cell's value (0 or 1)
        #         currentCell = board[i][j]
        #         # initialize an array to store the values of the 8 neighboring cells
        #         surroundings = [0 for _ in range(8)]
        #         # check each surrounding cell for its current state and update surroundings
        #         if i-1 >= 0 and j-1 >= 0: # up left
        #             surroundings[0] = board[i-1][j-1]
        #         if i-1 >= 0: # up
        #             surroundings[1] = board[i-1][j]
        #         if i-1 >= 0 and j+1 < n: # up right
        #             surroundings[2] = board[i-1][j+1]
        #         if j-1 >= 0: # left
        #             surroundings[3] = board[i][j-1]
        #         if j+1 < n: # right
        #             surroundings[4] = board[i][j+1]
        #         if i+1 < m and j-1 >= 0: # down left
        #             surroundings[5] = board[i+1][j-1]
        #         if i+1 < m: # down
        #             surroundings[6] = board[i+1][j]
        #         if i+1 < m and j+1 < n: # down right
        #             surroundings[7] = board[i+1][j+1]
        #         # if the current cell is dead (0), it becomes alive if exactly 3 neighbors are alive
        #         if currentCell == 0:
        #             if sum(surroundings) == 3:
        #                 tempArray[i][j] = 1  # mark the cell to be flipped (alive)
        #         else: # current cell is alive (1)
        #             # if fewer than 2 or more than 3 neighbors are alive, it dies
        #             if sum(surroundings) < 2 or sum(surroundings) > 3:
        #                 tempArray[i][j] = 1  # mark the cell to be flipped (dead)
        # # update the board based on the tempArray
        # for i in range(m):
        #     for j in range(n):
        #         if tempArray[i][j] == 1:  # if marked for flipping
        #             # flip the cell's value (dead to alive or alive to dead)
        #             if board[i][j] == 0:
        #                 board[i][j] = 1  # dead to alive
        #             else:
        #                 board[i][j] = 0  # alive to dead