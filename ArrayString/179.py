class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Approach 1: custom sort after multiply by 10
        # time O(n*k*logn), space O(n*k) where where n = len(nums), and k is the average number of digits in each number
        # convert the list of integers to a list of strings
        strNums = list(map(str, nums))
        # sort the string numbers using a custom key
        # the key function multiplies each string by 10 to repeat its pattern
        # this helps to ensure that numbers are compared in a way that maximizes the final concatenated result
        strNums.sort(key=lambda x: x * 10, reverse=True)
        # concatenate all the sorted string numbers to form the largest number
        largestNum = ''.join(strNums)
        # handle the case where the largest number is zero (e.g., when the input is [0, 0])
        # if the first character is '0', it means all numbers were zeros, so return '0'
        if largestNum[0] == '0':
            return '0'
        # return the concatenated result as the largest number
        return largestNum



        # # Approach 2: pass 156/232, does not capture the lexicographical comparison
        # # define a function to calculate the sum of the digits with zeros subtracting 1 from the sum
        # def sumOfDigitsWithZeroPenalty(n):
        #     sumDigits = 0
        #     for digit in str(n):
        #         if digit == '0':
        #             sumDigits -= 1  # subtract 1 for each zero
        #         else:
        #             sumDigits += int(digit)  # add the digit to the sum
        #     return sumDigits
        # # filter all numbers into 10 categories of digits
        # digitDict = {}
        # for num in nums:
        #     currentFirstDigit = str(num)[0]
        #     if currentFirstDigit not in digitDict:
        #         digitDict[currentFirstDigit] = []
        #     digitDict[currentFirstDigit].append(num)
        # # print(digitDict)
        # output = ""
        # # rank the digits in each sector
        # for i in range(9, -1, -1):
        #     key = str(i)
        #     if key in digitDict:
        #         identicalLenadingNums = digitDict[key]
        #         sortedNumbers = sorted(identicalLenadingNums, key=sumOfDigitsWithZeroPenalty, reverse=True)
        #         # print(sortedNumbers)
        #         for n in sortedNumbers:
        #             output += str(n)
        # return output