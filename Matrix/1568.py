class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        numRows = len(grid)  # get the number of rows in the grid
        numCols = len(grid[0])  # get the number of columns in the grid
            
        def countIslands():
            visited = set()  # create a set to track visited cells
            numIslands = 0  # initialize the number of islands to 0
            # both approaches have time O((numRows * numCols)^2), space O(numRows * numCols)

            # Approach 1: bfs
            def bfs(row, col):
                queue = deque([(row, col)])  # initialize the queue with the starting cell
                visited.add((row, col))  # mark the starting cell as visited
                while queue:
                    row, col = queue.popleft()  # pop the first element in the queue
                    # explore the four possible directions (up, down, left, right)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        newRow, newCol = row + dx, col + dy
                        # check if the new position is within bounds, is land, and hasn't been visited
                        if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                            visited.add((newRow, newCol))  # mark the new cell as visited
                            queue.append((newRow, newCol))  # add the new cell to the queue



            # Approach 2: dfs
            def dfs(row, col):
                # base cases: if out of bounds, water cell, or already visited
                if row < 0 or row >= numRows or col < 0 or col >= numCols or grid[row][col] == 0 or (row, col) in visited:
                    return
                visited.add((row, col))  # mark the cell as visited
                # recursively visit all adjacent land cells
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)

            # iterate through all cells in the grid
            for i in range(numRows):
                for j in range(numCols):
                    # if the cell is land and not yet visited, perform dfs
                    if grid[i][j] == 1 and (i, j) not in visited:
                        bfs(i, j)
                        # dfs(i, j)
                        numIslands += 1  # increment island count
            return numIslands  # return the total number of islands
        
        # initial check: if the grid is already disconnected, return 0
        if countIslands() != 1:
            return 0
        
        # try removing each land cell one by one
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:  # if the cell is land
                    grid[i][j] = 0  # temporarily remove the land cell
                    # check if this removal disconnects the grid
                    if countIslands() != 1:
                        return 1  # if disconnected, return 1
                    grid[i][j] = 1  # restore the cell      
        # if no single cell removal disconnects the island, return 2
        return 2