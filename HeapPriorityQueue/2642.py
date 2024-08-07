class Graph:
    # Approach 1: list of list with dijkstra algo
    # both approaches have time O((n+e)logn) and space O(n+e) where e = number of edges
    # log(n) is due to priority queue operations (push and pop) because in worst case the new element is moved up through all levels of the binary heap
    def __init__(self, n: int, edges: List[List[int]]):
        # adjacency list to represent the graph
        self.adjacencyList = [[] for _ in range(n)]
        # constructor to initialize the graph with nodes and edges
        for edge in edges:
            self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    # add a new edge to the graph
    def addEdge(self, edge: List[int]):
        self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    # find the shortest path between two nodes using Dijkstra's algorithm
    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)

    # Dijkstra's algorithm to find the shortest path
    def dijkstra(self, start: int, end: int) -> int:
        n = len(self.adjacencyList)
        distances = [float('inf')] * n
        distances[start] = 0
        # priority queue to efficiently retrieve the node with the minimum distance
        priorityQueue = [(0, start)]
        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)
            # skip if a shorter path has already been found
            if currentCost > distances[currentNode]:
                continue
            # if found the target node then return the cost
            if currentNode == end:
                return currentCost
            # explore neighbors and update distances
            for edge in self.adjacencyList[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]
                # update distance if a shorter route is found
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))
        # return the minimum distance or -1 if no path exists
        return -1 if distances[end] == float('inf') else distances[end]



    # # Approach 2: dict and bfs with priority queue
    # def __init__(self, n: int, edges: List[List[int]]):
    #     # initialize the graph with given number of nodes and edges
    #     self.directedWeightedGraph = defaultdict(list)
    #     for edge in edges:
    #         self.addEdge(edge)

    # def addEdge(self, edge: List[int]) -> None:
    #     # add an edge to the graph
    #     source, destination, weight = edge
    #     self.directedWeightedGraph[source].append((destination, weight))
    #     # ensure the destination node exists in the graph
    #     if destination not in self.directedWeightedGraph:
    #         self.directedWeightedGraph[destination] = []

    # def shortestPath(self, node1: int, node2: int) -> int:
    #     # check if both nodes are in the graph
    #     if node1 in self.directedWeightedGraph and node2 in self.directedWeightedGraph:
    #         # priority queue to store (current cumulative weight, current node)
    #         priorityQueue = [(0, node1)]
    #         visited = set()
    #         while priorityQueue:
    #             currentWeight, currentNode = heapq.heappop(priorityQueue)
    #             if currentNode == node2:
    #                 return currentWeight  # return the cumulative weight when the destination is reached
    #             visited.add(currentNode)
    #             for nextStop, weight in self.directedWeightedGraph[currentNode]:
    #                 if nextStop not in visited:
    #                     heapq.heappush(priorityQueue, (currentWeight + weight, nextStop))
    #     # special case when the start and end nodes are the same
    #     elif node1 == node2:
    #         return 0
    #     return -1  # return -1 if there is no path between node1 and node2

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)