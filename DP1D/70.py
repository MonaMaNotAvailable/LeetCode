class Solution:
    def climbStairs(self, n: int) -> int:
        # approach 1: 1d dp table, time O(n), space O(n)
        dp = [0] * (n+1)  # create a dp table to store results for subproblems
        dp[0] = 1  # base case: 1 way to climb 0 stairs
        dp[1] = 1  # base case: 1 way to climb 1 stair
        
        for i in range(2, n+1):  # iterate from the 2nd to nth stair
            dp[i] = dp[i-1] + dp[i-2]  # the number of ways to reach the ith stair is the sum of the ways to reach (i-1)th and (i-2)th stairs
        return dp[n]  # return the result stored at the nth index
        
        # space optimization alternative, time O(n), space O(1)
        # prev, curr = 1, 1  # initialize two variables to store the number of ways to reach (i-1)th and ith stairs
        # for i in range(2, n+1):  # iterate from the 2nd to nth stair
        #     temp = curr  # temporarily store the current value
        #     curr = prev + curr  # update curr to be the sum of prev and curr
        #     prev = temp  # update prev to the old value of curr
        # return curr  # return the current value which holds the result



        # approach 2: use permutations, time O(n), space O(1)
        # output = 1  # initialize output with 1, since one way is just taking 1 step n times
        # for i in range(1, n//2+1):  # loop through half the number of stairs to consider combinations of 1s and 2s
        #     output += int(math.factorial(n-i)/(math.factorial(i)*math.factorial(n-2*i)))  # calculate the number of ways to arrange the combination of 1s and 2s
        # return output  # return the total number of ways
