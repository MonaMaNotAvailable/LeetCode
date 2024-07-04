class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Approach 1: queue, time O(n), space O(n)
        q = deque()  # queue to store indices of characters
        arr = [0] * 26  # array to store counts of each character
        # iterate over the string
        for i in range(len(s)):
            q.append(i)  # push the index onto the queue
            arr[ord(s[i]) - ord('a')] += 1  # increment the count of the character
            # manage the queue to keep the first unique character at the front
            while q:
                if arr[ord(s[q[0]]) - ord('a')] > 1:
                    q.popleft()  # remove the index if the character is not unique
                else:
                    break  # break if the character at the front is unique
        if not q:
            return -1  # return -1 if no unique character is found
        return q[0]  # return the index of the first unique character



        # # Approach 2: fixed-size list, time O(n), space O(1)
        # idx = 10**5  # initialize idx to a large value
        # for i in string.ascii_lowercase:  # iterate over each letter in the alphabet
        #     x = s.find(i)  # find the first occurrence of the character
        #     if x != -1 and s.rfind(i) == x:  # check if the character occurs only once
        #         idx = min(idx, x)  # update idx to the smallest index of a unique character
        # return idx if idx != 10**5 else -1  # return the smallest index or -1 if no unique character is found



        # # Approach 3: map, time O(n), space O(n)
        # count = {}  # dictionary to keep track of character counts
        # for char in s:
        #     if char not in count:
        #         count[char] = 1  # if character is not in dictionary, add it with count 1
        #     else:
        #         count[char] += 1  # if character is already in dictionary, increment its count
        # # second iteration to find the first unique character
        # for i, char in enumerate(s):
        #     if count[char] == 1:  # find the first character with a count of 1
        #         return i  # return the index of the first unique character
        # # Original alternative:
        # # for key, item in count.items():
        # #     if item == 1:  # find the first character with a count of 1
        # #         return s.index(key)  # return the index of the first unique character
        # return -1  # return -1 if no unique character is found