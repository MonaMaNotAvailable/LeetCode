# Approach 1: binary search, time O(nlogn+mlogn) = sorting + bi-search for each prefix
# where n = len(products) and m = len(searchWord), space O(n+m)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()  # Sort by increasing lexicographical order of products
        ans = []
        prefix = ""
        beginSearch = 0
        
        for c in searchWord:
            prefix += c
            # perform binary search to find the starting index
            insertIndex = self.findInsertIndex(products, prefix, beginSearch, n)
            beginSearch = insertIndex
            suggestProducts = []
            for i in range(insertIndex, min(insertIndex + 3, n)):
                if products[i].startswith(prefix):
                    suggestProducts.append(products[i])
            ans.append(suggestProducts)
        return ans
    
    def findInsertIndex(self, products: List[str], prefix: str, low: int, high: int) -> int:
        # binary search to find the leftmost index to insert the prefix
        while low < high:
            mid = (low + high) // 2
            if products[mid] < prefix:
                low = mid + 1
            else:
                high = mid
        return low



# # Approach 2: Trie (prefix tree), time O(nlogn+nL+m) = sorting + insertion + search
# # where L = len(product), space O(nL+m)
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.words = []
        
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         root = TrieNode()
#         output = []
#         products.sort() # ensure the trie stores words in lexicographical order

#         # insert all products into the trie
#         for product in products:
#             tempNode = root
#             for letter in product:
#                 # create a new TrieNode if the letter does not exist
#                 if letter not in tempNode.children:
#                     tempNode.children[letter] = TrieNode()
#                 tempNode = tempNode.children[letter] # move to the child node & get to deeper level
#                 # the product is only added to the current node's words list if less than 3 products, not the parent node
#                 if len(tempNode.words) < 3:
#                     tempNode.words.append(product)

#         # search within the trie
#         tempNode = root
#         for letter in searchWord:
#             # avoid the 'NoneType' object has no attribute 'children' error by checking tempNode before accessing its children
#             if tempNode and letter in tempNode.children:
#                 tempNode = tempNode.children[letter]
#                 output.append(tempNode.words)
#             else:
#                 output.append([]) # append an empty list if the letter is not found
#                 tempNode = None # stop furthur search by setting tempNode to None
        
#         return output       



# The binary search approach has a better time complexity for product insertion and search, while the trie approach has a better time complexity for searching each prefix but can consume more space due to the trie structure.