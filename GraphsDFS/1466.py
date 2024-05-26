class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Approach1: adjacency list & dfs
        # Python integers are immutable: count = 0 -> count = [0]
        count = [0]
        visit = set()

        adj = [[] for _ in range(n)]
        for a,b in connections:
            adj[a].append((b, True))
            adj[b].append((a, False))

        def dfs(node, count):
            visit.add(node)
            for neighbor, outgoing in adj[node]:
                if neighbor not in visit:
                    if outgoing:
                        count[0] += 1
                    dfs(neighbor, count)  

        dfs(0, count)
        return count[0]


        # # Approach2: TLE, pass 75/76, BFS(process connections as a queue) 
        # visited = [False]*n
        # output = 0

        # while len(connections)!=0:
        #     currentEdge = connections.pop(0)
        #     # new branch
        #     if 0 in currentEdge:
        #         if currentEdge[0]==0: # wrong direction from the start
        #             output+=1
        #             node = currentEdge[1]
        #         else: # correct direction from the 1st edge
        #             node = currentEdge[0]
        #         visited[node] = True
        #     else:
        #         start = currentEdge[0]
        #         end = currentEdge[1]
        #         # wrong direction
        #         if visited[start]:
        #             output+=1
        #             visited[end] = True
        #         # correct direction
        #         elif visited[end]:
        #             visited[start] = True
        #         else:
        #             connections.append(currentEdge)
        
        # return output