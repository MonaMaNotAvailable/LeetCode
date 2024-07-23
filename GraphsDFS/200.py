class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1: dfs, time and space both O(m*n)
        # get the dimensions of the grid
        numRows = len(grid)
        numCols = len(grid[0])
        # set to keep track of visited cells
        visited = set()
        # initialize the count of islands
        numIslands = 0
        # helper function to perform dfs
        def dfs(row: int, col: int):
            # if the cell is out of bounds or already visited or water, return
            if row < 0 or row >= numRows or col < 0 or col >= numCols or grid[row][col] == '0' or (row, col) in visited:
                return
            # mark the cell as visited
            visited.add((row, col))
            # explore the adjacent cells
            dfs(row + 1, col)  # down
            dfs(row - 1, col)  # up
            dfs(row, col + 1)  # right
            dfs(row, col - 1)  # left 
        # iterate through each cell in the grid
        for i in range(numRows):
            for j in range(numCols):
                # start a dfs if the cell is land and not visited
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    numIslands += 1  # each dfs completes one island
        # return the total number of islands
        return numIslands



        # # Approach 2: bfs
        # # initialize the count of islands
        # result = 0
        # # set to keep track of visited cells
        # visited = set()
        # # queue to explore the extent of the current island
        # currentIsland = deque()
        # # get the dimensions of the grid
        # m = len(grid)
        # n = len(grid[0])
        # # iterate through each cell in the grid
        # for i in range(m):
        #     for j in range(n):
        #         # if the cell is land and not visited
        #         if grid[i][j] == "1" and (i, j) not in visited:
        #             # add the cell to the queue and mark it as visited
        #             currentIsland.append((i, j))
        #             # perform bfs to explore the entire island
        #             while currentIsland:
        #                 location = currentIsland.popleft()
        #                 row = location[0]
        #                 col = location[1]
        #                 # explore the cell below
        #                 if row + 1 < m:
        #                     if grid[row + 1][col] == "1" and (row + 1, col) not in visited:
        #                         visited.add((row + 1, col))
        #                         currentIsland.append((row + 1, col))
        #                 # explore the cell to the right
        #                 if col + 1 < n:
        #                     if grid[row][col + 1] == "1" and (row, col + 1) not in visited:
        #                         visited.add((row, col + 1))
        #                         currentIsland.append((row, col + 1))
        #                 # explore the cell to the left
        #                 if col - 1 >= 0:
        #                     if grid[row][col - 1] == "1" and (row, col - 1) not in visited:
        #                         visited.add((row, col - 1))
        #                         currentIsland.append((row, col - 1))
        #                 # explore the cell above
        #                 if row - 1 >= 0:
        #                     if grid[row - 1][col] == "1" and (row - 1, col) not in visited:
        #                         visited.add((row - 1, col))
        #                         currentIsland.append((row - 1, col))
        #             # increment the island count after fully exploring one island
        #             result += 1
        #         # mark the current cell as visited
        #         visited.add((i, j))
        # # return the total number of islands
        # return result