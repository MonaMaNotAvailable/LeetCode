class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Approach 1: min heap adds pairs based on the indices of the popped pair from both nums1 and nums2
        # time O(klogk), space O(k)
        # result list to store the k smallest pairs
        res = []
        # min-heap to keep track of the next smallest pair sum and their indices
        heap = []
        # push the first pair (sum, index in nums1, index in nums2) into the heap
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        # iterate k times or until the heap is empty
        for _ in range(k):
            # pop the smallest pair from the heap
            sum_, i, j = heapq.heappop(heap)
            # add the current smallest pair to the result list
            res.append([nums1[i], nums2[j]])
            # if there are more elements in nums1 and we are at the first element of nums2,
            # push the next pair from nums1 into the heap
            if i + 1 < len(nums1) and j == 0:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            # if there are more elements in nums2, push the next pair from nums2 into the heap
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res



        # # Approach 2: min heap to maintain the next smallest pair at the top by advancing index of nums2
        # time O(klogk), space O(k)
        # # create a min-heap to keep track of the next smallest pair
        # minHeap = []
        # # initialize the heap with the smallest pairs formed by the first k elements of nums1 and the first element of nums2
        # for i in range(min(k, len(nums1))):  # only need first k numbers in nums1
        #     heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
        # result = []
        # while k > 0:
        #     # extract the smallest sum from the heap (which gives the smallest pair currently)
        #     sum_, i, j = heapq.heappop(minHeap)
        #     # add this pair to the result list
        #     result.append([nums1[i], nums2[j]])
        #     # if there are more elements in nums2 for the current i (i.e., j + 1 is within bounds), push the next pair (nums1[i], nums2[j + 1]) into the heap
        #     if j + 1 < len(nums2):
        #         heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
        #     k -= 1
        # return result



        # # Approach 3: generate all pairs, MLE: pass 19/30
        # time O((m*n)log(m*n)), space O(m*n)
        # heap = []
        # heapq.heapify(heap)
        # for u in nums1:
        #     for v in nums2:
        #         heapq.heappush(heap, (u+v,[u,v]))
        # output = []
        # for _ in range(k):
        #     smallest = heapq.heappop(heap)
        #     output.append(smallest[1])
        # return output        