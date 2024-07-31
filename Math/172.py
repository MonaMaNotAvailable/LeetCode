class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Approach 1: reducing n, time O(log(n)), space O(1)
        zeroCount = 0  # initialize the count of trailing zeroes
        powerOfFive = 5  # start with the smallest power of 5
        # loop to count the number of factors of 5 in n!
        while n >= powerOfFive:
            zeroCount += n // powerOfFive  # add the number of multiples of the current power of 5
            powerOfFive *= 5  # move to the next power of 5
        return zeroCount



        # # Approach 2: count the existance of 5, time O(n), space O(1)
        # # if n is less than 5, there are no trailing zeroes in n!
        # if n < 5:
        #     return 0
        # countFive = 0  # initialize the count of factors of 5
        # # iterate through each number from 5 to n
        # for num in range(5, n + 1):
        #     # if the number is divisible by 5, it contributes to the count of trailing zeroes
        #     if num % 5 == 0:
        #         countFive += 1
        #         # check if the number is also divisible by higher powers of 5
        #         if num % 25 == 0:
        #             countFive += 1
        #             if num % 125 == 0:
        #                 countFive += 1
        #                 if num % 625 == 0:
        #                     countFive += 1
        #                     if num % 3125 == 0:
        #                         countFive += 1
        # return countFive