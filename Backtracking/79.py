class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Early return tricks
        # 1. If the word length exceeds the total number of cells, it's impossible
        if len(word) > m * n:
            return False
        
        # 2. Count the frequency of characters in the board
        count = Counter(sum(board, []))
        
        # If any character in the word has more occurrences than in the board, return False
        for char, countInWord in Counter(word).items():
            if count[char] < countInWord:
                return False
        
        # 3. Heuristic: reverse the word if the last character is less frequent than the first
        # This minimizes the search paths by starting with rarer characters
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]



        m, n = len(board), len(board[0])  # dimensions of the board
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        # Approach 1: dfs, time O(M×N×4^L) where L=len(word), space O(L)
        def dfs(r, c, index):
            # base case: all characters in the word have been matched
            if index == len(word):
                return True
            
            # boundary check and matching current character
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            
            # mark the current cell as visited by modifying the board temporarily
            temp = board[r][c]
            board[r][c] = "#"  # any symbol to mark as visited
            
            # recursively explore all 4 directions
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True
            
            # backtrack: restore the original value of the cell
            board[r][c] = temp
            return False
        
        # iterate over each cell in the grid as the starting point
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:  # potential starting point
                    if dfs(i, j, 0):
                        return True
        
        return False



        # # Approach 2: bfs, time O(M×N×4^L) where L=len(word), space O(M×N+L)
        # def bfs(start_r, start_c):
        #     # Queue holds tuples of (r, c, index, visited path)
        #     queue = deque([(start_r, start_c, 0, set([(start_r, start_c)]))])
            
        #     while queue:
        #         r, c, index, visited = queue.popleft()
                
        #         # If we matched the entire word
        #         if index == len(word) - 1:
        #             return True
                
        #         # Explore all 4 directions
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
                    
        #             # Check bounds, if cell matches the next character, and if it's not visited
        #             if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and board[nr][nc] == word[index + 1]:
        #                 # Create a new visited set for this path
        #                 new_visited = visited | {(nr, nc)}
        #                 queue.append((nr, nc, index + 1, new_visited))
            
        #     return False
        
        # # Start BFS from each cell that matches the first character of the word
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == word[0]:  # potential starting point
        #             if bfs(i, j):
        #                 return True
        
        # return False



        # # My approach: pass 73/87
        # m = len(board)
        # n = len(board[0])
        # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # maxDepth = len(word)

        # for i in range(m):
        #     row = board[i]
        #     for j in range(n):
        #         cell = row[j]
        #         # find the letter that matches the first one
        #         if cell == word[0]:
        #             if maxDepth == 1:
        #                 return True
        #             depth = 1
        #             currentPosition = (i, j)
        #             # avoid cycle
        #             visited = set() 
        #             visited.add(currentPosition)
        #             # bfs to find the right adjacent cell
        #             queue = deque([currentPosition])
        #             while queue:
        #                 step = len(queue)
        #                 for _ in range(step):
        #                     temp = queue.popleft()
        #                     (r, c) = temp
        #                     for dr, dc in directions:
        #                         nr, nc = r + dr, c + dc
        #                         # if the move is within bounds and not visited
        #                         if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
        #                             print(nr, nc, depth)
        #                             if board[nr][nc] == word[depth]:
        #                                 queue.append((nr, nc))
        #                                 visited.add((nr,nc))
        #                 if queue:
        #                     depth += 1
        #                 if depth == maxDepth:
        #                     return True
        # return False