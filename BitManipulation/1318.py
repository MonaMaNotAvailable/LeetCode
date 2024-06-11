class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Approach 1: using bitmask, time & space O(1)
        # 0 if equal, 1 if differ
        equal = (a | b) ^ c
        ans = 0
        for i in range(31):
            # create a bitmask with a 1 at the ith position
            mask = 1 << i
            # if the ith bit of equal is 1, indicating a difference at this position
            if equal & mask > 0:
                if c & mask:
                    # if the ith bit in c is 1, we need at least one bit in a or b to be 1
                    ans += 1
                else:
                    # if the ith bit in c is 0, we need both bits in a and b to be 0
                    ans += (a & mask > 0) + (b & mask > 0)
        return ans



        # # Approach 2: my solution, string comparison, time & space O(1)
        # # function to convert an integer to a 30-bit binary string
        # def digToBi(num:int) -> string:
        #     output = ""
        #     for i in range(29, -1, -1):
        #         temp = num-2**i
        #         if temp >= 0: #if num is greater than or equal to 2^i, set the bit to 1 and reduce num
        #             output += "1" 
        #             num = temp
        #         else: #if num is less than 2^i, set the bit to 0
        #             output += "0" 
        #     return output
        
        # aString, bString, cString = digToBi(a), digToBi(b), digToBi(c)
        # result = 0
        # # iterate through each bit position from 29 to 0
        # for j in range(29, -1, -1):
        #     if int(cString[j]) != int(bString[j])|int(aString[j]):
        #         # if both bits in a and b are 1 and the bit in c is 0, we need 2 flips
        #         if int(bString[j])==1 and int(aString[j])==1:
        #             result += 2
        #         else:
        #             result += 1
        # return result



        # # Approach 3: from the least significant bit (LSB) to the most significant bit (MSB) to determine the number of flips
        # result = 0
        # for i in range(30):  # 30 bits to cover the range of input values
        #     # shifts the bits of a to the right by i positions and then extracts the least significant bit (LSB) using the bitwise AND operation with 1
        #     # extract bits at position i
        #     bitA = (a >> i) & 1
        #     bitB = (b >> i) & 1
        #     bitC = (c >> i) & 1
            
        #     if bitC == 0:
        #         result += bitA + bitB  # Both bits should be 0
        #     else:
        #         if bitA == 0 and bitB == 0:
        #             result += 1  # At least one bit should be 1
                
        # return result