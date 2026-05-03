class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # approach 1: greedy with binary search, time O(nlogn), space O(n)
        sub = []  # this list will store the smallest possible tail value for increasing subsequences
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                # if sub is empty or the last element of sub is smaller than the current number, append x
                sub.append(x)
            else:
                # find the index of the first element in sub that is greater than or equal to x
                index = bisect_left(sub, x)
                # replace that element with x to maintain the smallest possible values in sub
                sub[index] = x
        # the length of sub will be the length of the longest increasing subsequence
        return len(sub)



        # approach 1.1: a concise version, time O(nlogn), space O(n)
        # `piles` is a patience-sorting structure. It does NOT store the actual LIS — only its length is meaningful. Piles is always sorted in ascending order.
        piles = []

        for n in nums:
            # Binary search for the leftmost position where piles[idx] >= n. This is where n can "replace" to keep piles as small as possible, which leaves more room for future numbers to extend the sequence.
            idx = bisect.bisect_left(piles, n)

            if idx == len(piles):
                # n is larger than everything in piles, it genuinely extends the longest subsequence found so far.
                piles.append(n)
            else:
                # n fits somewhere in the middle (or at the front). Replace piles[idx] with n to "lower the ceiling" at this length, making it easier for future numbers to continue a subsequence of the same or greater length.
                piles[idx] = n

        # len(piles) equals the length of the LIS.
        return len(piles)
    


        # approach 2: dp, time O(n^2), space O(n)
        n = len(nums)
        dp = [1] * n  # initialize dp array where each element starts with length 1 (itself)
        for i in range(n):
            for j in range(i):
                # if nums[i] can extend the subsequence ending at nums[j]
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1  # update dp[i] with the max possible subsequence length
        # the maximum value in dp array will be the length of the longest increasing subsequence
        return max(dp)



        # approach 3: direct comparison, time O(n^2), space O(n)
        n = len(nums)
        output = [1 for _ in range(n)]  # initialize output array to store max subsequence length at each index
        for i in range(1, n):
            currentNum = nums[i]  # current number to compare
            for j in range(0, i):
                if currentNum > nums[j]:
                    # update output[i] with the maximum length subsequence ending at nums[i]
                    output[i] = max(output[i], output[j]+1)
        # the maximum value in the output array will be the length of the longest increasing subsequence
        return max(output)