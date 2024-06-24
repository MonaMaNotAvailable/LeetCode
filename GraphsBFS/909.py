class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Approahch 1: bfs & flattens the 2D board into a 1D list
        n = len(board)
        # preprocess the board to create a list of values corresponding to each cell number
        cells = [-1] * (n * n + 1)  # initialize a list to hold cell values; -1 indicates no ladder/snake
        index = 1  # start indexing from 1 to match cell numbers
        for i in range(n-1, -1, -1):  # traverse rows from bottom to top
            row = board[i]
            if (n - i) % 2 == 0:  # if the row number is even (considering bottom to top)
                row = row[::-1]  # reverse the row to match the zigzag pattern
            for j in range(n):  # iterate over columns
                cells[index] = row[j]  # map the board value to the cell index
                index += 1  # move to the next cell

        # bfs initialization
        nextMoves = deque([1])  # start BFS from cell 1
        visited = {1: 0}  # dictionary to keep track of the minimum steps to reach each cell, starting with cell 1
        
        while nextMoves:
            curr = nextMoves.popleft()  # get the current cell to process
            for num in range(curr + 1, min(curr + 6, n * n) + 1):  # simulate dice roll (1 to 6 steps)
                next_val = cells[num]  # get the board value at the target cell
                if next_val == -1:  # if there's no snake or ladder at the target cell
                    next_val = num  # move to the target cell itself
                # if the next cell is not visited or can be reached in fewer steps, process it
                if next_val not in visited or visited[next_val] > visited[curr] + 1:
                    visited[next_val] = visited[curr] + 1  # update steps to reach this cell
                    nextMoves.append(next_val)  # add the next cell to the queue
                    if next_val == n * n:  # if we reach the last cell, return the steps count
                        return visited[next_val]
        return -1  # return -1 if the last cell is not reachable



        # # Approach 2: bfs & function to match board value
        # # time O(n^2), space O(n^2)
        # n = len(board)
        # def getBoardValue(num):
        #     """get the board value at the given cell number"""
        #     # calculate row and column from the cell number
        #     # divmod: returns quotient and remainder in a tuple
        #     r, c = divmod(num - 1, n)
        #     if r % 2 == 0:
        #         c = c  # if even row, use column as is
        #     else:
        #         c = n - 1 - c  # if odd row, reverse the column index
        #     # get the value from the board, adjusting row to match bottom-to-top layout
        #     return board[n - 1 - r][c]
        # # bfs initialization
        # nextMoves = deque([1])  # start from cell 1
        # visited = {1: 0}  # keep track of the minimum steps to reach each cell
        # while nextMoves:
        #     curr = nextMoves.popleft()  # get the current cell
        #     for num in range(curr + 1, min(curr + 6, n**2) + 1):
        #         nextVal = getBoardValue(num)  # get the board value for the next cell
        #         if nextVal == -1:
        #             nextVal = num  # if there's no snake or ladder, move to the cell itself
        #         # if the next cell is not visited or can be reached in fewer steps, process it
        #         if nextVal not in visited or visited[nextVal] > visited[curr] + 1:
        #             visited[nextVal] = visited[curr] + 1  # update steps to reach this cell
        #             nextMoves.append(nextVal)  # add the next cell to the queue
        #             if nextVal == n**2:  # if we reach the last cell, return the steps count
        #                 return visited[nextVal]
        # return -1  # return -1 if the last cell is not reachable



        # # Approach 3: bfs & pre-computed index for each number, pass 200/215
        # n = len(board)
        # # calculate cell index for each number from 1 to n**2
        # numRowIndex = []
        # numColIndex = [j for j in range(0, n)]
        # k = n
        # for i in range(1, n**2+1, n):
        #     k-=1
        #     for _ in range(n):
        #         numRowIndex.append(k)
        # for _ in range(n-1):
        #     numColIndex.extend(reversed(numColIndex[-n:]))
        # # print(numRowIndex)
        # # print(numColIndex)
        # nextMoves = deque([1])
        # visited = set([1])
        # output = 0
        # while n**2 not in visited:
        #     output += 1
        #     for _ in range(len(nextMoves)):
        #         nextDestination = nextMoves.popleft()
        #         for num in range(nextDestination+1, min(nextDestination+6, n**2)+1):
        #             if num not in visited:
        #                 if board[numRowIndex[num-1]][numColIndex[num-1]] == -1:
        #                     nextMoves.append(num)
        #                     visited.add(num)
        #                 else:
        #                     nextMoves.append(board[numRowIndex[num-1]][numColIndex[num-1]])
        #                     visited.add(board[numRowIndex[num-1]][numColIndex[num-1]])
        #     if set(nextMoves) == visited and n**2 not in visited:
        #         return -1
        #     # print(nextMoves)
        # return output        