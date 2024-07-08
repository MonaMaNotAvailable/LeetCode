class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Apporach 1: one pointer and divmod
        aL, bL = -len(a), -len(b)  # calculate negative lengths for iteration
        i, carry, res = -1, 0, ""  # initialize index, carry, and result string
        while i >= aL or i >= bL:  # loop while there are digits to process in either string
            aBit = int(a[i]) if i >= aL else 0  # get the bit from a or 0 if index is out of bounds
            bBit = int(b[i]) if i >= bL else 0  # get the bit from b or 0 if index is out of bounds
            # add the values along with the carry, and compute the new carry and remainder
            carry, remainder = divmod(aBit + bBit + carry, 2)
            res = str(remainder) + res  # determine the result bit and prepend it to the result string
            i -= 1  # move to the next bit to the left
        return "1" + res if carry else res  # if there's a remaining carry, prepend it to the result



        # # Approach 2: padding with list
        # # make the lengths of a and b the same by padding with zeroes
        # sameLength = max(len(a), len(b))
        # a = a.zfill(sameLength)
        # b = b.zfill(sameLength)
        # result = ["0"]*(sameLength+1)
        # # iterate over the strings from the end to the beginning
        # for i in range(sameLength-1, -1, -1):
        #     # if both characters are the same
        #     if a[i] == b[i]:
        #         if a[i] == "1": # both 1
        #             result[i] = "1"
        #         # else both 0, pass
        #     else: # one character is 1 and the other is 0
        #         if result[i+1] == "1": # if there's a carry
        #             result[i] = "1"
        #             result[i+1] = "0"
        #         else:
        #             result[i+1] = "1"
        # # if the most significant bit is 0, remove it
        # if result[0] == "0":
        #     result.pop(0)
        # # join the list into a string and return
        # return ''.join(result)