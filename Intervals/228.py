class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Approach 1: pointer, time O(n) & space O(n)
        output = []
        n = len(nums)
        # initialize index pointer
        i = 0
        
        while i < n:
            # store the start of the current range
            start = nums[i]
            # increment index while the next number is consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            # store the end of the current range
            end = nums[i]
            # append the range to output list as a single number if start equals end
            if start == end:
                output.append(str(start))
            # otherwise append the range in the format start->end
            else:
                output.append(f"{start}->{end}")
            # increment index to check the next potential range
            i += 1
    
        return output



        # # Approach 2: intervals & post-processing
        # ranges = []  # initialize an empty list to store ranges as [start, end]
    
        # for n in nums:
        #     # if ranges is not empty and the last range ends just before the current number
        #     if ranges and ranges[-1][1] == n - 1:
        #         # extend the last range to include the current number
        #         ranges[-1][1] = n
        #     else:
        #         # otherwise, start a new range [n, n]
        #         ranges.append([n, n])

        # # format the ranges for output
        # return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]