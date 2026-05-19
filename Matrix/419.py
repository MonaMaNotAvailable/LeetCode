class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Approach 1: Count the top-left cells of each battleship, time O(m*n), space O(1)
        m = len(board)
        n = len(board[0])
        count = 0

        for r in range(m):
            for c in range(n):
                # only process battleship cells
                if board[r][c] == 'X':

                    # skip if part of a vertical ship
                    if r > 0 and board[r - 1][c] == 'X':
                        continue

                    # skip if part of a horizontal ship
                    if c > 0 and board[r][c - 1] == 'X':
                        continue

                    # top-left start of a new ship
                    count += 1

        return count
    


        # Approach 2: DFS, time O(m*n), space O(m*n)
        m = len(board)
        n = len(board[0])
        visited = set()
        count = 0

        def dfs(r, c):
            # out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            # stop if water or already visited
            if board[r][c] != 'X' or (r, c) in visited:
                return

            visited.add((r, c))

            # explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):

                # found a new battleship
                if board[r][c] == 'X' and (r, c) not in visited:
                    count += 1
                    dfs(r, c)

        return count