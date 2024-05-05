# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    
        # Approach 1: using bst & find the min successor
        if not root:
            return None
        
        # Find the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Find the smallest node in its right subtree
            temp = self.findMin(root.right)
            # Prepare for deletion
            root.val = temp.val
            # Find and delete the node with the duplicate value
            root.right = self.deleteNode(root.right, root.val)
        
        return root
    
    def findMin(self, node):
        current = node
        # The smallest value in any subtree is found at the leftmost 
        while current.left:
            current = current.left
        return current



        # # Approach2: did not consider 2 children, only pass 22/92
        # def traverse(node: Optional[TreeNode], prevNode: Optional[TreeNode], prevSide: int):
        #     if not node:
        #         return
        #     print(node.val)

        #     # if the matching one is found
        #     if node.val == key:
        #         # create a branch for replacement
        #         if node.left:
        #             if prevSide == -1:
        #                 prevNode.left = node.left
        #             elif prevSide == 1:
        #                 prevNode.right = node.left
        #         elif node.right:
        #             if prevSide == 1:
        #                 prevNode.right = node.right
        #             elif prevSide == -1:
        #                 prevNode.left = node.right
        #         else:
        #             node.val = None
        #     else:
        #         prevNode = node
        #     if node.left:
        #         traverse(node.left, node, -1)
        #     if node.right:
        #         traverse(node.right, node, 1)
        
        # traverse(root, root, 0)
        # return root