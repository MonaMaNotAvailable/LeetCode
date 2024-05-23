class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Approach 1: use a list of bool to keep track of visited
        n = len(isConnected)
        visit = [False]*n

        def dfs(u):
            for v in range(n):
                if not visit[v] and isConnected[u][v] ==1:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if not visit[i]:
                count += 1
                visit[i] = True
                dfs(i)
        
        return count



        # # Approach 2: use set
        # n = len(isConnected)
        # visitedCity = set()
        # output = 0

        # # Given an city, return list of neighbors it visited
        # def recursiveConnection(city: int):
        #     for neighbor in range(n):
        #         if neighbor not in visitedCity and isConnected[city][neighbor]==1:
        #             visitedCity.add(neighbor)
        #             recursiveConnection(neighbor)

        # # generate list of list to record cities & visited
        # for i in range(n):
        #     if i not in visitedCity:
        #         visitedCity.add(i)
        #         # recursively find connected cities -> DFS
        #         recursiveConnection(i)
        #         output+=1

        # # return the length of the disjoint sets
        # return output