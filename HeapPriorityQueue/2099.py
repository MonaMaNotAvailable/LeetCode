class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: min-heap
        # time O(nlogk) due to pushing n items into the heap, space O(k)
        # create a heap to store the top k largest elements with their indices
        heap = []
        # iterate through the array
        for index, num in enumerate(nums):
            heapq.heappush(heap, (num, index))
            if len(heap) > k:
                heapq.heappop(heap)
        # sort the heap by index to maintain original order
        heap.sort(key=lambda x: x[1])
        # extract the elements to form the subsequence
        return [nums[index] for (num, index) in heap]



        # # Approach 2: sort and concatenate and sort
        # # time O(nlogn) due to sorting tuples, space O(n)
        # # create a list of tuples containing each element and its index
        # values = [(num, i) for (i, num) in enumerate(nums)]
        # # sort the list in descending order based on the element values
        # values.sort(reverse=True)
        # # select the first k elements (these are the k largest elements)
        # maxs = values[:k]
        # # sort the selected elements by their original index to maintain order
        # maxs.sort(key=lambda x : x[1])
        # # extract the elements to form the subsequence
        # return [num for (num, i) in maxs]



        # # Approach 3: linear scan with replacement
        # # time O(n*k) since finding and replacing the minimum occurs for each element, space O(k)
        # output = []
        # # iterate through the array
        # for num in nums:
        #     # if the output list has less than k elements, add the current element
        #     if len(output)<k:
        #         output.append(num)
        #     else:
        #         # find the minimum element in the output list
        #         currentMin = min(output)
        #         # if the current element is larger than the minimum, replace it
        #         if num > currentMin:
        #             output.pop(output.index(currentMin))
        #             output.append(num)
        # # return the output list as the subsequence
        # return output