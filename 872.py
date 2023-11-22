# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #Approach 1: combine list & go into None node
        def dfs(root):
            if not root: return []
            if not root.left and not root.right:
                return [root.val] 
            return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)

        #Approach 2: handle None before going into the branch
        # def helper(node) -> list :
        #     if node.left == None and node.right == None:
        #         return [node.val]
        #     else:
        #         lSeq = helper(node.left) if node.left else []
        #         rSeq = helper(node.right) if node.right else []
        #         return lSeq+rSeq
        
        # seq1 = helper(root1)
        # seq2 = helper(root2)
        # return seq1 == seq2