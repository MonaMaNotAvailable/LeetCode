class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Approach 1: 1D array, time O(m x n), space O(n)
        # initialize the 1st row
        dp = [1] * n
        # from the second row
        for i in range(1, m):
            for j in range(1, n):
                # the sum of the ways from above and to the left
                dp[j] += dp[j - 1]
        # the last cell
        return dp[-1]



        # # Approach 2: 2D array, time O(m x n), space O(m x n)
        # # represents the number of ways to reach each cell
        # array2D = [[1]*n for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         # the sum is the cell directly above it and to the left
        #         array2D[i][j] = array2D[i-1][j]+array2D[i][j-1]
        # # value in the bottom-right corner
        # return array2D[m-1][n-1]



# The solution is exactly Pascal's Triangle
# m/n 1 2 3 4 5
#   1 1 1 1 1 1
#   2 1 2 3 4 5
#   3 1 3 6 10
#   4 1 4 10 20
#   5 1 5



        # # Approach 3: brute-force dfs, without @cache -> TLE: pass 37/63
        # # time O(2^(m+n-2)) because at each cell, there are 2 possible recursive calls
        # # space O(m+n-2): the depth/length of the path

        # # @cache #from functools in Pythoon 3.9: caches the results of function calls and reuses these results when the same inputs occur again
        # def dfs(i, j):
        #     if i >= m or j >= n:      
        #         return 0
        #     if i == m-1 and j == n-1: 
        #         return 1
        #     return dfs(i+1, j) + dfs(i, j+1)
        # return dfs(0, 0)



        # # Approach 4: combinatorial, time O(m+n-2), space O(1)
        # # total number of moves: m+n−2 = m-1 down moves + n-1 right moves
        # # return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
        # return comb(m + n - 2, m - 1)