class TrieNode:
    def __init__(self):
        self.children = {}  # dictionary to hold child nodes
        self.is_end_of_word = False  # flag to mark the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # root node of the trie

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()  # create a new node if the character is not already present
            current = current.children[char] # moves the current pointer to the newly created node (or the existing node if it was already present), advances to the next level in the trie
        current.is_end_of_word = True  # mark the end of the word

    def longest_common_prefix(self) -> str:
        current = self.root
        prefix = ""
        while current and len(current.children) == 1 and not current.is_end_of_word:
            char = next(iter(current.children))  # get the only child character
            prefix += char  # add the character to the prefix
            current = current.children[char]  # move to the next node
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Approach 1: Trie, time O(n*m), space O(n*m)
        if not strs:
            return ""  # return empty string if the input list is empty
        # create a trie instance
        trie = Trie()  
        for word in strs:
            trie.insert(word)  # insert each word into the trie
        return trie.longest_common_prefix() 



        # # Approach 2: brute-force matching / vertical scanning, time O(n*m), space O(1)
        # # find the length of the shortest string in the list to avoid index out of bound
        # minLength = min(len(s) for s in strs)
        # output = ""
        # for i in range(minLength):
        #     currrentChar = strs[0][i]
        #     for str in strs:
        #         # compare the current character from the first string with the same position character in other strings
        #         if str[i]!= currrentChar:
        #             # a mismatch is found, return the output so far
        #             return output
        #     # if no mismatch, append the current character to the output
        #     output += currrentChar
        # return output



        # # Approach 3: compare first & last items without sorting, time O(n+m), space O(1)
        # ans = ""
        # # get the first and last string in lexicographical order without sorting
        # first = min(strs)
        # last = max(strs)
        # # iterate through the characters of the shortest string between the first and last
        # for i in range(min(len(first), len(last))):
        #     # if characters do not match, return the result so far
        #     if first[i] != last[i]:
        #         return ans
        #     # if characters match, add the character to the result
        #     ans += first[i]
        # return ans