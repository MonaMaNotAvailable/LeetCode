class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Approach 1: a global depth variable for BFS
        rows, cols = len(maze), len(maze[0])
        visited = set() # avoid cycle
        visited.add((entrance[0], entrance[1]))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        depth = 0

        # bfs, add possible next move to the queue
        queue = deque([entrance]) # starting position
        while queue:
            step = len(queue)
            for _ in range(step):
                temp = queue.popleft()
                r, c = temp[0], temp[1]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if the move is within bounds and not visited
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if maze[nr][nc] == '.':
                            # check if at border
                            if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                                if [nr, nc] != entrance:
                                    return depth + 1
                            # border but not exit
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            depth+=1
        # base case
        return -1



        # # Approach 2: integrate the depth directly into the BFS queue
        # queue = deque([(entrance[0], entrance[1], 0)]) # starting position
        # # bfs, add possible next move to the queue
        # while queue:
        #     r, c, distance = queue.popleft()
        #     for dr, dc in directions:
        #         nr, nc = r + dr, c + dc
        #         # if the move is within bounds and not visited
        #         if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
        #             if maze[nr][nc] == '.':
        #                 # check if at border
        #                 if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
        #                     if [nr, nc] != entrance:
        #                         return distance + 1
        #                 # border but not exit
        #                 queue.append((nr, nc, distance + 1))
        #                 visited.add((nr, nc))
        # # base case
        # return -1