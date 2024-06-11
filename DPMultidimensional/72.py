class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Approach 1: recursion with memoization dictionary to store results of subproblems, time & space O(MN)
        memo = {}
        
        def helper(w1, w2):
            # if result is already in memo, return it
            if (w1, w2) in memo:
                return memo[(w1, w2)]
            # base cases
            if not w1 and not w2:
                return 0
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)
            # if first characters are the same, no additional operation is needed
            if w1[0] == w2[0]:
                memo[(w1, w2)] = helper(w1[1:], w2[1:])
            else:
                # calculate minimum operations for insert, delete, and replace
                # insert the first character of word2 (w2[0]) into word1
                insert = 1 + helper(w1, w2[1:])
                # delete the first character of word1 (w1[0])
                delete = 1 + helper(w1[1:], w2)
                # replace the first character of word1 (w1[0]) with the first character of word2 (w2[0])
                replace = 1 + helper(w1[1:], w2[1:])
                memo[(w1, w2)] = min(insert, delete, replace)
            return memo[(w1, w2)]
        # call the helper function with the original words
        return helper(word1, word2)



        # # Approach 2: 2D DP, time & space O(MN)
        # m, n = len(word1), len(word2)
        # # dp[i][j] holds the minimum edit distance between word1[:i] and word2[:j]
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # # initialize the first column and the first row of the DP table
        # for i in range(m + 1):
        #     dp[i][0] = i # if word2 is empty, we need i deletions to convert word1[:i] to word2
        # for j in range(n + 1):
        #     dp[0][j] = j # if word1 is empty, we need j insertions to convert word1 to word2[:j]
        
        # # fill the DP table
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             # if the characters are the same, no additional operation is needed
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             # If the characters are different, consider the minimum of the three operations:
        #             # 1. Substitution (dp[i-1][j-1])
        #             # 2. Deletion from word1 (dp[i-1][j])
        #             # 3. Insertion into word1 (dp[i][j-1])
        #             dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) 
        #             dp[i][j] += 1 # add 1 to the minimum of these values to account for the current operation
        
        # # The value in dp[m][n] is the minimum edit distance between the entire word1 and word2
        # return dp[m][n]



        # # Approach 3: post-processing by optimizing the replace operation, pass 570/1146
        # # try replace everything then optimize, incorrect due to ignoring dependencies between operations
        # replaceOperation = []
        # insertOperation = []
        # deleteOperation = []

        # for i in range(len(word1)):
        #     if i < len(word2): #if exists
        #         if word1[i] != word2[i]:
        #             replaceOperation.append((word1[i], word2[i]))
        #     else:
        #         deleteOperation.append(word1[i])
        
        # if len(word1) < len(word2):
        #     for j in range(len(word1), len(word2)):
        #         insertOperation.append(word2[j])
        
        # # print(replaceOperation)
        # # print(insertOperation)
        # # print(deleteOperation)

        # index = 0
        # for originalChar, newChar in replaceOperation:
        #     if originalChar in insertOperation:
        #         replaceOperation.pop(index)
        #     if newChar in deleteOperation:
        #         replaceOperation.pop(index)
        #     index += 1

        # return len(replaceOperation)+len(insertOperation)+len(deleteOperation)