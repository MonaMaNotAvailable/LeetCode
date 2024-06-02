class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Approach 1: sort based on num2, min-heap to track the largest k elements of num1, sliding sum

        # combine into list of tuples
        combined = list(zip(nums1, nums2))
        # sort based on nums2 in descending order
        combined.sort(key=lambda x: -x[1])

        # Min-heap to keep track of the largest k elements from nums1
        minHeap = []
        currentSum = 0
        maxScore = 0

        for num1, num2 in combined:
            # add num1 to heap and update the current sum
            heapq.heappush(minHeap, num1)
            currentSum += num1

            # remove the smallest element if the heap size exceeds k 
            # only consider distinct states of num1's combination
            if len(minHeap) > k:
                currentSum -= heapq.heappop(minHeap)

            # update the max score If exactly k elements
            if len(minHeap) == k:
                # print(minHeap)
                maxScore = max(maxScore, currentSum * num2)

        return maxScore



        # # Approach 2: TLE: pass 12/28, try all combination of num1
        # self.currentMax = 0

        # def backTrack(index: List[int], start:int):
        #     if len(index) == k:
        #         tempSum = sum(nums1[i] for i in index)
        #         tempMin = min(nums2[i] for i in index)
        #         self.currentMax = max(self.currentMax, tempSum * tempMin)
        #     else:
        #         for j in range(start, len(nums1)):
        #             index.append(j)
        #             backTrack(index, j+1)
        #             index.pop()
        
        # backTrack([], 0)
        # return self.currentMax