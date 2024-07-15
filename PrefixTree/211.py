class WordDictionary:
    # Approach 1: Trie, high time complexity for searching words with many wildcards
    def __init__(self):
        self.trie = {}  # nested dictionary to store the trie structure
        
    def addWord(self, word: str) -> None: #time O(n), space O(t), where t = the total number of characters in all the words
        # iterative approach to add a word to the trie
        node = self.trie
        # build dict like this {'a': {'p': {'p': {'l': {'e': {'#': True}}}}}}
        for char in word:
            if char not in node:
                node[char] = {}
            # move to the next node in the trie
            node = node[char]
        node['#'] = True  # use a special character to mark the end of a word
        
    def search(self, word: str) -> bool: #time O(26^n), space O(n) due to recursion
        # call the helper function to search in the trie
        return self.searchInNode(word, self.trie)
    
    def searchInNode(self, word: str, node: dict) -> bool:
        # iterate over the characters in the word
        for i, char in enumerate(word):
            # if the character is not in the current node
            if char not in node:
                # if the character is a wildcard '.', check all possible nodes
                if char == '.':
                    for x in node:
                        # skip the special end-of-word character and recursively search the remaining part of the word
                        if x != '#' and self.searchInNode(word[i + 1:], node[x]):
                            return True
                # if the character is not found and is not a wildcard, return false
                return False
            else:
                # move to the next node in the trie
                node = node[char]
        # check if the current node marks the end of a word
        return '#' in node



    # # Approach 2: set, storing multiple patterns for each word
    # def __init__(self):
    #     self.data = set()  # initialize a set to store words and patterns

    # def addWord(self, word: str) -> None: #time O(n), space O(w*n), where w = the total number of words, n = the average length of the words
    #     self.data.add(word)  # add the full word to the set
    #     # add patterns with one wildcard (.) to the set
    #     for i in range(len(word)):
    #         self.data.add(word[:i] + "." + word[i + 1:])

    # def search(self, word: str) -> bool: #time O(26^k) where k = number of wildcards, space O(1)
    #     if word in self.data:
    #         return True  # if the word or pattern is in the set, return true
    #     if word.count(".") != 2: 
    #         # there will be at most 2 dots in word for search queries, if more than 2, we need to
    #         # implement a recursive or iterative approach that can systematically replace each wildcard
    #         return False  # if the word does not contain exactly two wildcards, return false

    #     # check all possible replacements for the wildcard
    #     for c in "abcdefghijklmnopqrstuvwxyz":
    #         if word.replace(".", c, 1) in self.data:
    #             return True  # if any replacement of the first wildcard is in the set, return true

    #     return False  # if no matches are found, return false
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)