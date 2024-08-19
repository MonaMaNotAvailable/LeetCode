class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Approach 1: heap, time O(nlogn), space O(n)
        # calculate the frequency of absolute differences between nums1 and nums2
        # we only consider non-zero differences
        freq = Counter(abs(x1 - x2) for x1, x2 in zip(nums1, nums2) if x1 != x2)
        # create a max heap from the frequency counter
        # heap stores negative differences (to simulate max heap) and their corresponding frequencies
        pq = [(-k, v) for k, v in freq.items()]
        heapify(pq)
        # combine the number of allowed modifications (k1 and k2)
        k1 += k2
        # while there are still elements in the heap and modifications available
        while pq and k1:
            # pop the largest element (in terms of absolute difference) from the heap
            x, v = heappop(pq)
            # check if there is another element in the heap
            if pq:
                # get the next largest element
                xx, vv = heappop(pq)
            else:
                # if no more elements, set next element values to 0
                xx = vv = 0
            # calculate the difference between the largest and the next largest elements
            diff = xx - x
            # if we can reduce all occurrences of the largest element to the next largest element
            if diff * v <= k1:
                # decrease the available modifications
                k1 -= diff * v
                # if the next largest element exists, combine the frequencies and push back to heap
                if vv:
                    heappush(pq, (xx, v + vv))
            else:
                # if not enough modifications to reduce all occurrences of the largest element
                # distribute the remaining modifications as evenly as possible
                q, r = divmod(k1, v)
                k1 = 0
                # push the updated elements back to the heap
                heappush(pq, (x + q + 1, r))  # for the part with remainder modifications
                heappush(pq, (x + q, v - r))  # for the rest that were evenly reduced
                # if the next largest element exists, push it back to the heap
                if vv:
                    heappush(pq, (xx, vv))
        # calculate the final sum of squared differences
        return sum(x * x * v for x, v in pq)



        # # Approach 2: aggregated reduction that keeps track of the largest number and its count, time O(nlogn), space O(n)
        # # combine the number of allowed modifications from both k1 and k2
        # k = k1 + k2
        # # calculate the absolute differences between nums1 and nums2
        # # exclude pairs where the difference is zero
        # nums = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2) if num1 - num2 != 0]
        # # add a zero to the list to handle the final reduction case uniformly
        # nums.append(0)
        # # sort the differences in descending order
        # nums.sort(reverse=True)
        # # initialize the largest number (leftNum) and its count (leftCnt)
        # leftNum, leftCnt = nums[0], 1
        # # iterate through the sorted differences
        # for i in range(1, len(nums)):
        #     # calculate the total difference that can be reduced with the current leftCnt
        #     d = (leftNum - nums[i]) * leftCnt
        #     if d <= k:
        #         # if we can reduce all occurrences of the current max difference to the next level
        #         k -= d  # subtract the used modifications
        #         leftNum, leftCnt = nums[i], leftCnt + 1  # update leftNum and increase leftCnt
        #     else:
        #         # if not enough modifications to reduce all occurrences to the next level
        #         leftNum -= k // leftCnt  # evenly distribute the remaining modifications
        #         r = k % leftCnt  # calculate the remainder of modifications
        #         # calculate the final sum of squared differences
        #         return leftNum**2 * (leftCnt - r) + (leftNum - 1)**2 * r + \
        #                sum(num**2 for num in nums[i:])
        # # if all differences are reduced to zero, return 0
        # return 0



        # # Approach 3: TLE, pass 30/38, time O(n^2), space O(n)
        # n = len(nums1)
        # # calculate the absolute differences between nums1 and nums2
        # diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        # # total number of modifications allowed
        # modifyChances = k1 + k2
        # # if we have enough modifications to reduce all differences to zero, return 0
        # if modifyChances >= sum(diff):
        #     return 0
        # # sort the differences in descending order
        # diff.sort(reverse=True)
        # # iterate through the sorted differences
        # for i in range(n):
        #     # find the next lower value in the list (or 0 if at the end of the list)
        #     nextValue = diff[i+1] if i < n-1 else 0
        #     # calculate the maximum possible reduction for the current segment
        #     maxReduce = diff[i] - nextValue
        #     maxReduceCount = (i + 1)  # number of elements with the current max value
        #     # total reduction possible by reducing all current max elements to the next value
        #     totalReduce = maxReduce * maxReduceCount
        #     if modifyChances >= totalReduce:
        #         # reduce all elements in the current segment to the next lower value
        #         for j in range(i + 1):
        #             diff[j] -= maxReduce
        #         # subtract the used modifications
        #         modifyChances -= totalReduce
        #     else:
        #         # evenly distribute the remaining reductions
        #         fullReduce = modifyChances // maxReduceCount
        #         remainderReduce = modifyChances % maxReduceCount
        #         # apply full reduction to each element in the current segment
        #         for j in range(i + 1):
        #             diff[j] -= fullReduce
        #         # apply the remainder reductions one by one
        #         for j in range(remainderReduce):
        #             diff[j] -= 1
        #         # no more modifications available
        #         modifyChances = 0
        #         break
        # # calculate the sum of squared differences
        # output = sum(x * x for x in diff)
        # return output