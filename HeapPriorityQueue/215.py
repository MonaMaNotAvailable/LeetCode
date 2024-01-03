class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        return self.quick_select(nums, k, 0, len(nums) - 1)
        
    def quick_select(self, nums, k, start, end):
        if start == end:
            return nums[k - 1]
        l, r = start, end
        mid = l + (r - l) // 2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if r >= k - 1:
            return self.quick_select(nums, k, start, r)
        if l <= k - 1:
            return self.quick_select(nums, k, l, end)
        return nums[r + 1]


        #Memory Limit Exceeded
        # head = []
        # tail = []
        # for n in nums:
        #     if n >= nums[-1]:
        #         head.append(n)
        #     else:
        #         tail.append(n)
        
        # # print(head)
        # if len(head) == k:
        #     return nums[-1]
        # elif len(head) < k:
        #     return self.findKthLargest(tail, k-len(head))
        # else:
        #     return self.findKthLargest(head[0:len(head)-1], k)

        #pivot = nums[-1]
        # head_count = sum(1 for n in nums if n >= pivot)
        
        # if head_count == k:
        #     return pivot
        # elif head_count < k:
        #     # Recursively search in the tail part of the list
        #     tail_nums = [n for n in nums if n < pivot]
        #     return self.findKthLargest(tail_nums, k - head_count)
        # else:
        #     # Recursively search in the head part of the list without the pivot
        #     head_nums = [n for n in nums if n >= pivot]
        #     return self.findKthLargest(head_nums[0:-1], k)