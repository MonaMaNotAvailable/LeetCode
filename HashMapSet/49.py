class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # approach 1: create a dictionary to store grouped anagrams
        # anagram = {}
        # approach 2: using defaultdict to automatically create an entry for that key with a default value of an empty list
        # time O(k*nlogn), space O(k*n), where k = len(strs) and n = len(word)
        anagram = defaultdict(list)
        # iterate through each word in the input
        for word in strs:
            # sort the word and use it as a key for the dictionary
            key = ''.join(sorted(word))
            # # if the key doesn't exist, create a new list with the word
            # if key not in anagram:
            #     anagram[key] = []
            # append the word to the corresponding list
            anagram[key].append(word)
        return list(anagram.values())