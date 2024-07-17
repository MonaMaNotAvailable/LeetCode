# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Approach 1: dfs with range, ensures each node's value is correctly bounded by the values of its ancestors
        # time and space both O(n)
        def dfs(node: Optional[TreeNode], minValue: float, maxValue: float) -> bool:
            # if the current node is None, return True
            if not node:
                return True
            # if the current node's value does not lie within the valid range, return False
            if not (minValue < node.val < maxValue):
                return False
            # recursively check the left subtree with updated max value
            # and the right subtree with updated min value
            return dfs(node.left, minValue, node.val) and dfs(node.right, node.val, maxValue)
        # start the dfs with the root node and the initial range (-inf, inf)
        return dfs(root, float('-inf'), float('inf'))



        # # Approach 2: pass 77/85
        # # Wrong because this only checks the direct parent-child relationships. 
        # # It does not ensure that all values in the left subtree are less than the root, 
        # # and all values in the right subtree are greater than the root
        # def dfs(node: Optional[TreeNode], prevValue: int, branch: str) -> bool:
        #     flag = True
        #     if not node:
        #         # if the node is null, return true
        #         return flag
        #     if branch == "left":
        #         # if it's a left branch, check if the current node's value is less than the previous node's value
        #         flag = node.val < prevValue
        #     elif branch == "right":
        #         # if it's a right branch, check if the current node's value is greater than the previous node's value
        #         flag = prevValue < node.val
        #     leftTemp = True
        #     rightTemp = True
        #     if node.left:
        #         # recursively check the left subtree
        #         leftTemp = dfs(node.left, node.val, "left")
        #     if node.right:
        #         # recursively check the right subtree
        #         rightTemp = dfs(node.right, node.val, "right")
        #     # return true if the current node is valid and both left and right subtrees are valid
        #     return flag and leftTemp and rightTemp
        # # start the dfs with the root node
        # return dfs(root, 0, "")