class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Approach 1: KMP(Knuth–Morris–Pratt) pattern matching, , time O(m+n), space O(n)
        # helper function to compute the Longest Prefix Suffix (LPS) array
        def computeLPSArray(pattern):
            lps = [0] * len(pattern)  # initialize the LPS array with zeros
            length = 0  # length of the previous longest prefix suffix
            i = 1  # start from the second character of the pattern
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    # if characters match, increment the length and set the LPS value
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        # if there's a mismatch, use the previous LPS value to avoid redundant comparisons
                        length = lps[length - 1]
                    else:
                        # if no previous match, set LPS to 0 and move to the next character
                        lps[i] = 0
                        i += 1
            return lps
        # Preprocess the needle to get the LPS array
        lps = computeLPSArray(needle)
        i = 0  # index for haystack
        j = 0  # index for needle
        while i < len(haystack):
            if needle[j] == haystack[i]: # if characters match, move both indices forward
                i += 1
                j += 1
            if j == len(needle): # reached the end of the needle, a match is found
                return i - j  # return the start index
            elif i < len(haystack) and needle[j] != haystack[i]:
                # if there's a mismatch after some matches
                if j != 0:
                    # use the LPS array to skip characters in the needle
                    j = lps[j - 1]
                else:
                    # if no previous match, move the haystack index forward
                    i += 1
        # If no match is found, return -1
        return -1



        # # Approach 2: simple matching, time O(m*n), space O(1)
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        
        # return -1