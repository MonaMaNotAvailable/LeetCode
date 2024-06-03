class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach 1: two pointers without sorting (check in-place)
        # Initialize pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            
            # move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # convert to lowercase and compare characters (case insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # move pointers inward
            left += 1
            right -= 1
        
        return True



        # # Approach2: parse and then two pointers
        # tempString = ""

        # punctuations = string.punctuation + " "
        # for letter in s:
        #     if letter not in punctuations:
        #         tempString += letter.lower()
        
        # print(tempString)
        # start = 0
        # end = len(tempString)-1

        # while start < end:
        #     if tempString[start] != tempString[end]:
        #         return False
        #     else:
        #         start+=1
        #         end-=1
                
        # return True




        # # Approach 3 by ChatGPT: reverse the string
        # # create a filtered, lowercase string without punctuations and spaces
        # # isalnum(): built-in method that returns True if all characters in the string are alphanumeric
        # tempString = ''.join([char.lower() for char in s if char.isalnum()])
        
        # # if the string is a palindrome using slicing
        # return tempString == tempString[::-1]