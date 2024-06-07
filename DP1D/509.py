class Solution:
    def fib(self, n: int) -> int:
        # Approach 1: DP1D record the entire sequence of Fibonacci numbers up to n
        fibNums = [0,1]
        for _ in range(2,n+1):
            fibNums.append(fibNums[-2]+fibNums[-1])
        return fibNums[n]

        # # similarly, update in place by keeping the last 2 elements only
        # if n == 0:
        #     return 0
        # fibNums = [0,1]
        # for _ in range(2,n+1):
        #     fibNums = [fibNums[-1], fibNums[-2]+fibNums[-1]]
        # return fibNums[-1]



        # # Approach 2: try @cache again to compare with iterative approach
        # @cache
        # def recur(num):
        #     if num < 2:
        #         return num
        #     else:
        #         return recur(num-1)+recur(num-2)
        # return recur(n)



        # # Approach 3: Binet's formula 
        # # the conjugate of the golden ratio is a negative number with absolute value less than 1
        # # as n increases, conjugate^n appraoches 0 & becomes negligible, F(n) is approaximately goldenRatio^n/sqrt(5)
        # goldenRatio = (1 + sqrt(5)) / 2
        # return int((goldenRatio ** n + 1) / sqrt(5))