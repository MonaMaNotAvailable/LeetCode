class SmallestInfiniteSet:
    # Apprach 1: using a min-heap, O(log n) time complexity for both insertion and removal of the smallest element
    def __init__(self):
        # maintain a set for O(1) average-time complexity for membership checks and deletions
        self.available = set()
        # set to list
        self.heap = []
        # track the next smallest number to return after the initial set is exhausted
        self.minNum = 1
    
    def popSmallest(self) -> int:
        if self.heap:
            # removes and returns the smallest element from the heap, the root node
            smallest = heapq.heappop(self.heap)
            # sync the set
            self.available.remove(smallest)
            return smallest
        # empty heap, return the next smallest number and increment it
        smallest = self.minNum
        self.minNum += 1
        return smallest

    def addBack(self, num: int) -> None:
        # if not already in the set & smaller than minNum
        if num < self.minNum and num not in self.available:
            # add the number back to the set of available numbers
            self.available.add(num)
            # push the number back into the min-heap
            heapq.heappush(self.heap, num)
    


    # # Approach 2: not initializing a large set & use set only
    # def __init__(self):
    #     self.curMin = 1
    #     self.infPosSet = set()

    # def popSmallest(self) -> int:
    #     if self.infPosSet:
    #         res = min(self.infPosSet)
    #         self.infPosSet.remove(res)
    #         return res
    #     else:
    #         self.curMin += 1
    #         # the next smallest integer that hasn't been popped yet
    #         return self.curMin - 1

    # def addBack(self, num: int) -> None:
    #     if self.curMin > num:
    #         # only numbers that have been popped can be added back
    #         self.infPosSet.add(num) 



    # # Approach 3: my slowest solution
    # def __init__(self):
    #     self.set = set([i for i in range(1, 1000)])
    #     self.smallest = 1

    # def popSmallest(self) -> int:
    #     if self.smallest in self.set: # avoid key error
    #         self.set.remove(self.smallest)
    #     tempSmallest = self.smallest
    #     # update the smallest in the set
    #     if self.set:
    #         self.smallest = min(self.set)
    #     else: # if set is empty, the next smallest integer should be one greater than the last removed smallest element
    #         self.smallest = tempSmallest+1
    #     return tempSmallest

    # def addBack(self, num: int) -> None:
    #     if num not in self.set:
    #         self.set.add(num)
    #         self.smallest = min(self.smallest, num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)