class Solution:
    def numTilings(self, n: int) -> int:
        # Approach 1: Time O(N), Space O(N), initialize list of zeros as place holders
        dp = [1, 2, 5] + [0] * (n-3)
        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % 1000000007
        return dp[n - 1]



        # # Approach 2: Time O(N), Space O(1), maintain minimal list possible
        # initial = [1, 1, 2]
        # MOD = 10**9 + 7

        # if n < 3:
        #     return initial[n]
        # else:
        #     for i in range(n-2):
        #         temp = (2*initial[2]+initial[0]) % MOD
        #         initial.pop(0)
        #         initial.append(temp)
        # return initial[-1]


	# for each dp[n], it can be constructed using:
	# dp[n-1] + {|}
	# dp[n-2] + {=}
	# dp[n-3] + {L reversed L}*2
	# dp[n-4] + {L = reversed L}*2
	# dp[n-5] + {[_]}*2
	#...
	# dp[n] = dp[n - 1] + dp[n - 2] + 2 * (dp[n - 3]...0) 
	# dp[n - 1] = dp[n - 2] + dp[n - 3] + 2 * (dp[n - 4]...0)
	# dp[n] - dp[n - 1] = dp[n - 1] + dp[n - 3]
	# dp[n] = 2 * dp[n - 1] + dp[n - 3]