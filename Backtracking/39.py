class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 1: dfs, index & sorting to avoid duplicates
        # time O(t^(n/m)) where t = target, n = len(candidates), & m = min(candidates), space O(t^(n/m))
        # store all the unique combinations that sum up to the target
        output = []
        # sort the candidates to ensure combinations are generated in non-decreasing order
        candidates.sort()
        # dfs traversal
        def dfs(start: int, remaining: int, currentCombination: List[int]):
            # if remaining is 0, we found a valid combination
            if remaining == 0:
                output.append(currentCombination[:])  # append a shallow copy of the current combination
                return
            # loop through the candidates starting from the current index
            for i in range(start, len(candidates)):
                num = candidates[i]
                # only proceed if the current candidate can be part of the combination
                if num <= remaining:
                    currentCombination.append(num)  # choose the current candidate
                    dfs(i, remaining - num, currentCombination)  # explore further with updated remaining
                    currentCombination.pop()  # backtrack and remove the last chosen candidate
        # start DFS with the initial parameters
        dfs(0, target, [])
        return output



        # # Approach 2: backtrack, create a list for each recursive call, time O(t^(n/m)), space O(t/m*n)
        # res = []  # This will store all unique combinations that sum up to the target
        # candidates.sort()  # Sort candidates to handle combinations in non-decreasing order
        
        # def dfs(target, index, path):
        #     if target < 0:
        #         return  # If the target becomes negative, no valid combination can be formed
        #     if target == 0:
        #         res.append(path)  # If the target is exactly 0, we found a valid combination
        #         return 
        #     for i in range(index, len(candidates)):
        #         # For each candidate starting from the current index, make a recursive call
        #         # Subtract the candidate value from the target and add the candidate to the path
        #         dfs(target - candidates[i], i, path + [candidates[i]])
        
        # dfs(target, 0, [])  # Start the DFS with the initial target, starting index, and empty path
        # return res



        # # Approach 3: dp, time O(n*t), space O(t×k), where k is the number of combinations for each target
        # # dp[i] will store all unique combinations that sum up to i
        # dp = [[] for _ in range(target + 1)]  
        # # iterate through each candidate
        # for c in candidates:
        #     # iterate through all possible target values from c to target
        #     for i in range(c, target + 1):
        #         # if i equals the candidate, it means we have a single-element combination
        #         if i == c:
        #             dp[i].append([c])
        #         # for each combination that sums up to (i - c)
        #         for comb in dp[i - c]:
        #             # append the current candidate to these combinations and add to dp[i]
        #             dp[i].append(comb + [c])
        # # the result is the list of combinations that sum up to the target
        # return dp[-1]