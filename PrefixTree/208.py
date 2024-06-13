class Trie:

    def __init__(self): #a dict of dict
        self.trie = {} # nested dictionary

    def insert(self, word: str) -> None: #time & space O(N) for both approaches
        # iterative approach
        node = self.trie
        # build dict like this {'a': {'p': {'p': {'l': {'e': {'#': True}}}}}}
        for char in word:
            if char not in node:
                node[char] = {}
            # key step to get to deeper level
            node = node[char]
        node['#'] = True  # use a special character to mark the end of a word

        # recursive approach
        # def recursive_insert(node, word):
        #     if not word:
        #         node['#'] = True  # End of word marker
        #         return
        #     if word[0] not in node:
        #         node[word[0]] = {}
        #     recursive_insert(node[word[0]], word[1:])
        # recursive_insert(self.trie, word)

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # if node['#']: # can lead to a KeyError if it doesn't exist
        #     return True
        # return False
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)