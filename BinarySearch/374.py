# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        lowerbound = 1
        upperbound = n

        while lowerbound <= upperbound:
            print(lowerbound, upperbound)
            half = (upperbound+lowerbound)//2
            print(half)

            ask = guess(half)
            print(ask)

            if ask == 0:
                return half
            elif ask == -1:
                upperbound = half-1
            elif ask == 1:
                lowerbound = half+1
            else:
                return 0


        # #does not terminate given ask == 0
        # half = n//2
        # print(half)

        # ask = guess(half)
        # print(ask)
        # print(ask == 0)

        # if ask == 0:
        #     print("Im here")
        #     print(type(half))
        #     return half
        # elif ask == -1:
        #     return self.guessNumber(half)
        # elif ask == 1:
        #     return self.guessNumber(half*3)
        # else:
        #     return 0