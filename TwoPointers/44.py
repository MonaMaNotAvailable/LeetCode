class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Approach 1: 2 pointers, time O(m×n), space O(1)
        # initialize pointers for the input string and the pattern
        string_index = 0
        pattern_index = 0
        # initialize pointers for the last character matched and the last '*' encountered in the pattern
        last_match_index = 0
        star_index = -1
        # loop through the input string
        while string_index < len(s):
            # check if the current characters in the input string and the pattern match, or if the pattern character is '?'
            if pattern_index < len(p) and (s[string_index] == p[pattern_index] or p[pattern_index] == '?'):
                # move the pointers for the input string and the pattern forward
                string_index += 1
                pattern_index += 1
            # check if the current pattern character is '*'
            elif pattern_index < len(p) and p[pattern_index] == '*':
                # store the current positions of the pointers for the input string and the pattern
                last_match_index = string_index
                star_index = pattern_index
                # move the pointer for the pattern forward
                pattern_index += 1
            # if none of the above conditions are met, check if we have encountered a '*' in the pattern previously
            elif star_index != -1:
                # move the pointer for the pattern back to the last '*'
                pattern_index = star_index + 1
                # move the pointer for the input string to the next character after the last character matched
                string_index = last_match_index + 1
                # move the pointer for the last character matched forward
                last_match_index += 1
            # if none of the above conditions are met, the input string and the pattern do not match
            else:
                return False
        # loop through the remaining characters in the pattern and check if they are all '*' characters
        while pattern_index < len(p) and p[pattern_index] == '*':
            pattern_index += 1
        # return True if all the characters in the pattern have been processed, False otherwise
        return pattern_index == len(p)



        # # Approach 2: 2D boolean dp table, time O(m×n), space O(mxn)
        # m, n = len(s), len(p)
        # # create a 2D dp array with default values as false
        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True  # both string and pattern are empty
        # # fill the first row for patterns with '*'
        # for j in range(1, n + 1):
        #     if p[j - 1] == '*':
        #         dp[0][j] = dp[0][j - 1]  # '*' can match an empty sequence
        # # fill the dp table
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] == '*':
        #             # '*' can match zero characters (dp[i][j-1]) or one/more characters (dp[i-1][j])
        #             dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        #         elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
        #             # '?' matches any single character, or current characters match
        #             dp[i][j] = dp[i - 1][j - 1]
        # return dp[m][n]  # result is in the bottom-right cell of the dp table



        # # Approach 3: recursion with memoization, time O(m×n), space O(mxn)
        # @lru_cache(None)
        # def match_from(i: int, j: int) -> bool:
        #     # base case: if we've reached the end of the pattern
        #     if j == len(p):
        #         # check if we've also reached the end of the string
        #         return i == len(s)
        #     # check if the current characters match or if the pattern has a '.'
        #     first_match = i < len(s) and (p[j] == s[i] or p[j] == '?' or p[j] == '*')
        #     # handle the '*' character
        #     if j < len(p) and p[j] == '*':
        #         # two cases: 
        #         # 1. we ignore the '*' and the preceding element in the pattern
        #         # 2. the '*' matches one or more characters in the string
        #         return match_from(i, j + 1) or (first_match and match_from(i + 1, j))
        #     else:
        #         # no '*' character, so move to the next character in both string and pattern
        #         return first_match and match_from(i + 1, j + 1)
        # # start the recursion from the beginning of both the string and the pattern
        # return match_from(0, 0)