class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # Approach 1: min-heap, time and space both O(n)
        alphabet = ascii_lowercase
        # initialize counters and a default dictionary
        ctr, dic = Counter(s), defaultdict(int)  # 'ctr' counts frequencies of each char in 's'; 'dic' to store final counts for replacements
        qmarks = ctr['?']  # number of '?' characters in the string
        rep = lambda x, y: x.replace('?', y, dic[y] - ctr[y])  # function to replace '?' with the correct character based on frequency
        # create a min-heap based on the frequency of each character in the alphabet
        heap = list(map(lambda x: (ctr[x], x), alphabet))  # map each character to a tuple of its count and the character itself
        heapify(heap)  # transform the list into a heap to allow efficient retrieval of the minimum frequency element
        # allocate '?' replacements by assigning the least frequent characters
        for _ in range(qmarks):
            cost, ch = heappop(heap)  # pop the character with the smallest frequency
            heappush(heap, (cost + 1, ch))  # push it back with an increased frequency to reflect its use in replacing '?'
        # update the dictionary with the final frequency counts after all '?' have been replaced
        for cost, ch in heap: 
            dic[ch] = cost  # store the final frequency for each character after replacing all '?'
        # replace all '?' in the original string with the correct characters based on the updated dictionary
        return reduce(rep, alphabet, s)  # apply the replacement function across all characters in the alphabet



        # # Approach 2: frequency array & manually find the least frequent character for each ?
        # # time O(nlogn), space O(n)
        # # initialize a frequency array for lowercase letters (a-z)
        # freq = [0] * 26  
        # temp = []  # list to store the characters replacing '?'
        # # calculate the frequency of each character in the string, excluding '?'
        # for c in s:
        #     if c != '?':
        #         freq[ord(c) - ord('a')] += 1  # increment the frequency for the current character
        # # iterate over the string to find and replace '?' characters
        # for ind in range(len(s)):
        #     if s[ind] != '?':
        #         continue  # skip non-'?' characters
        #     # find the character with the minimum frequency in the current state
        #     minFreq = sys.maxsize  # set to maximum possible value initially
        #     minFreqInd = 0  # index to track the character with minimum frequency
        #     # check all 26 lowercase letters to find the one with the lowest frequency
        #     for i in range(26):
        #         if minFreq > freq[i]:  # if the current character has a lower frequency
        #             minFreq = freq[i]  # update the minimum frequency
        #             minFreqInd = i  # update the index of the minimum frequency character
        #     # append the character with the minimum frequency to the temp list
        #     temp.append(chr(ord('a') + minFreqInd))
        #     freq[minFreqInd] += 1  # increment the frequency of the selected character
        # # sort the temp list to ensure lexicographical order
        # temp.sort()
        # # create a list from the string to allow modification
        # result = list(s)
        # j = 0  # index to track position in the temp list
        # # replace the '?' characters in the original string with sorted characters
        # for i in range(len(result)):
        #     if result[i] == '?':
        #         result[i] = temp[j]  # replace '?' with the corresponding character from temp
        #         j += 1  # move to the next character in temp
        # # convert the list back to a string and return the result
        # return ''.join(result)



        # # My approach: pass 156/548, does not take into account the frequency, lexicographical minimization is insufficient
        # # record the letters that exists
        # charSet = set()
        # # record the index of ?
        # questionMarkIndexes = []
        # for i in range(len(s)):
        #     char = s[i]
        #     if char == "?":
        #         questionMarkIndexes.append(i)
        #     else:
        #         charSet.add(char)
        # print(charSet)
        # print(questionMarkIndexes)
        # # filter out the available letters
        # option = deque()
        # for letter in string.ascii_lowercase:
        #     if letter not in charSet:
        #         option.append(letter)
        # print(option)
        # # convert the input string to list
        # output = list(s)
        # if len(option) >= len(questionMarkIndexes):
        #     # filled in the ? with letter that never appeared before
        #     for index in questionMarkIndexes:
        #         sub = option.popleft()
        #         output[index] = sub
        # else:
        #     # if all 26 letters exist, just filled in a to make it lexicographically the smallest
        #     for j in range(len(questionMarkIndexes)-1, -1, -1):
        #         sub = "a"
        #         if option:
        #             sub = option.pop()
        #         output[questionMarkIndexes[j]] = sub
        # return "".join(output)