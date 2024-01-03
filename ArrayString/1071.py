class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Longest repeated common substr        
        if str1+str2 != str2+str1:
            return ""
        else:
            return str1[:gcd(len(str1), len(str2))]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

        # pass 13/123, set does not preserve order, BAC CBA instead of ABC
        # if (str1 not in str2) and (str2 not in str1):
        #     return ""
        # elif set(str1) != set(str2):
        #     return ""
        # else:
        #     return "".join(set(str1).intersection(str2))