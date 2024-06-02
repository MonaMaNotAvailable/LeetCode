class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Approach: no need to maintain the same sizes for left & right min-heaps, use pointer to track next element to be added
        leftCandidates = costs[:candidates]
        # avoid overlap with left
        rightCandidates = rightCandidates = costs[max(candidates, len(costs) - candidates):]
        # convert lists into min-heaps, O(N)
        heapq.heapify(leftCandidates)
        heapq.heapify(rightCandidates)
        # use pointers for the next element to push to the heaps
        leftPtr = candidates
        rightPtr = len(costs) - candidates - 1
        # record output
        totalCosts = 0

        for _ in range(k):
            # compare the smallest from 2 min-heaps
            if leftCandidates and (not rightCandidates or leftCandidates[0] <= rightCandidates[0]):
                totalCosts += heapq.heappop(leftCandidates)
                # maintain the size by pushing the next element from the left side if any
                if leftPtr <= rightPtr:
                    heapq.heappush(leftCandidates, costs[leftPtr])
                    leftPtr += 1
            else:
                totalCosts += heapq.heappop(rightCandidates)
                # push the next element from the right side if any
                if rightPtr >= leftPtr:
                    heapq.heappush(rightCandidates, costs[rightPtr])
                    rightPtr -= 1
        return totalCosts