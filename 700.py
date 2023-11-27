# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        #Approach 1: time complexity is the height of the BST
        node=root
        while(node):
            if node.val==val:
                return node
            elif node.val<val:
                node=node.right
            else:
                node=node.left
        return None

        #Approach 2: recursive call, time complexity is n/2
        # if not root:
        #     return
        # elif root.val == val:
        #     return root
        # elif root.val > val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)