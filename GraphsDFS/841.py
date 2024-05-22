class Solution:
    # Approach 1: Recursion -- DFS
    def visitAll(self,rooms,index,visited):
        if index not in visited:
            visited.add(index)
            for i in rooms[index]:
                self.visitAll(rooms,i,visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.visitAll(rooms,0,visited)
        return len(visited)==len(rooms)
        
        

    # def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # # Approach 2: Queue -- BFS
        # # visited room 0 first to get the initial set of keys
        # visitedRooms = set([0])
        # keys = rooms[0]
        
        # # while there are keys we never used
        # while len(keys) != 0:
        #     # process the first key
        #     currentKey = keys.pop(0) 
        #     # only use the key if we never visit that room before
        #     if currentKey not in visitedRooms:
        #         # record to avoid repeated keys
        #         visitedRooms.add(currentKey)
        #         # get more keys
        #         moreKeys = rooms[currentKey] 
        #         keys.extend(moreKeys)
        
        # # if room visited equals to the room available, then we visited all of the rooms
        # if len(visitedRooms) == len(rooms):
        #     return True
        # return False



        # Approach 3: Stack -- DFS
        # visited_rooms = set()
        # stack = [0] 
        
        # while stack: 
        #     room = stack.pop() 
        #     visited_rooms.add(room)
        #     for key in rooms[room]:
        #         if key not in visited_rooms:
        #             stack.append(key)
        # return len(visited_rooms) == len(rooms) 