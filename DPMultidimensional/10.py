class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Approach 1: 2d dp table, time & space O(len(s)*len(p))
        # initialize the table with False, indicates whether the first i characters of s match the first j characters of p
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # an empty string matches an empty pattern

        # handle patterns like a*, a*b*, a*b*c* etc.
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                # match zero occurrence of the character before *
                dp[0][j] = dp[0][j - 2]  # dp[0][j - 2] corresponds to the scenario where this preceding character appears zero times

        # fill the dp table
        for i in range(1, len(s) + 1):
            print(dp)
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # current characters match, inherit the result from the previous state
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # * can mean zero occurrence of the character before it
                    dp[i][j] = dp[i][j - 2]
                    # * can also mean one or more occurrences of the character before it
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        # return the result for the full string and full pattern
        return dp[len(s)][len(p)]



        # # Approach 2: recursion, time O(2^(len(s)+len(p)), space O(len(s)*len(p))
        # @lru_cache(None)
        # def match_from(i: int, j: int) -> bool:
        #     # base case: if we've reached the end of the pattern
        #     if j == len(p):
        #         # check if we've also reached the end of the string
        #         return i == len(s)
            
        #     # check if the current characters match or if the pattern has a '.'
        #     first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
        #     # handle the '*' character
        #     if j + 1 < len(p) and p[j + 1] == '*':
        #         # two cases: 
        #         # 1. we ignore the '*' and the preceding element in the pattern
        #         # 2. the '*' matches one or more characters in the string
        #         return match_from(i, j + 2) or (first_match and match_from(i + 1, j))
        #     else:
        #         # no '*' character, so move to the next character in both string and pattern
        #         return first_match and match_from(i + 1, j + 1)
        
        # # start the recursion from the beginning of both the string and the pattern
        # return match_from(0, 0)



        # # Approach 3: can't handle cases like a*a, pass 285/356
        # chars = list(s)
        # for i in range(len(p)):
        #     if chars: #if s is not empty
        #         if p[i] == chars[0] or p[i] == ".":
        #             chars.pop(0)
        #         elif p[i] == "*":
        #             prevChar = p[i-1]
        #             while chars:
        #                 if prevChar == chars[0] or prevChar == ".":
        #                     chars.pop(0)
        #                 else:
        #                     break
        #     else:
        #         if p[i] != "." or p[i] != "*":
        #             return False
        # # check any element left
        # return chars == []