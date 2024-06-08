class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Approach 1: reusing previous results, time O(m*n)
        m, n = len(text1), len(text2)
        # initialize a 2D dp array with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # dp[i][j] represents the length of LCS of text1[0..i-1] and text2[0..j-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # extend the LCS found so far by 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # take the maximum LCS length possible by either excluding the current character of text1 or text2
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # for row in dp:
        #     print(row)
        return dp[m][n]



        # # Approach 2 TLE pass 15/27 time O((MN)^2)   
        # # find index of all matching pairs     
        # pairs = []
        # for i in range(len(text1)):
        #     for j in range(len(text2)):
        #         if text1[i] == text2[j]:
        #             pairs.append([i, j])
        # # print(pairs)

        # # find the longest increasing subsequence
        # n = len(pairs)
        # dp = [1] * n  # Initialize dp array with 1

        # for i in range(1, n):
        #     for j in range(i):
        #         if pairs[i][1] > pairs[j][1] and pairs[i][0] > pairs[j][0]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # # print(dp)
        # if dp:
        #     return max(dp)
        # return 0