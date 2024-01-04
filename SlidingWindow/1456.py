class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Approach 1: no need to maintain a queue, only keep the max count
        maxCount = 0
        eachCount = 0
        vowels = "aeiou"

        for i in range(len(s)):
            #add for all case
            eachCount += s[i] in vowels
            #minus except for base case
            if i >= k and s[i-k] in vowels:
                eachCount -= 1
            maxCount = max(maxCount, eachCount)
        return maxCount  



        # #Approach 2: maintain a queue and current max count
        # vowel = "aeiou"
        # queue = list(s[:k])
        # maxCount = 0

        # for char in queue:
        #     if char in vowel:
        #         maxCount+=1
        # #early stop: max reached
        # if maxCount == k:
        #     return maxCount

        # tempCount = maxCount
        # #slide through the str s with window size k
        # for i in range(k, len(s)):
        #     temp = queue.pop(0)
        #     if temp in vowel:
        #         tempCount -= 1
        #     #shift the window
        #     queue.append(s[i])
        #     if s[i] in vowel:
        #         tempCount += 1
        #     maxCount = max(maxCount, tempCount)
        #     #early stop: max reached
        #     if maxCount == k:
        #         return maxCount
        
        # return maxCount  



        # #Approach 3: a more concise version of 1
        # vowels = frozenset("aeiou")
        # cnt = ans = sum(s[i] in vowels for i in range(k))
        # if ans != k:
        #     for i in range(k, len(s)):
        #         cnt += (s[i] in vowels) - (s[i - k] in vowels)
        #         if (ans := max(cnt, ans)) == k:
        #             break
        # return ans