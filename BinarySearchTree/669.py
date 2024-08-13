# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Approach 1: recursive, time O(n), space O(n)
        if not root:
            return None  # base case should return None
        # if the current node's value is less than the low threshold, the trimmed binary search tree must be in the right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # if the current node's value is greater than the high threshold, the trimmed binary search tree must be in the left subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # recursively trim the left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root



        # # Approach 2: iterative, time O(n), space O(1)
        # # find a valid root that lies within the range [low, high], keep moving the root to the right if it's too small or to the left if it's too large
        # while root and (root.val < low or root.val > high):
        #     if root.val < low:
        #         root = root.right  # move to the right child if the root is too small
        #     elif root.val > high:
        #         root = root.left  # move to the left child if the root is too large
        # # if the root is None after adjustment, return None
        # if not root:
        #     return None
        # # trim the left subtree by checking if any left child node
        # # is out of the [low, high] range
        # current = root
        # while current:
        #     # if the left child's value is less than low, discard the left child
        #     while current.left and current.left.val < low:
        #         current.left = current.left.right  # move left pointer to the right child of the left node
        #     current = current.left  # move to the next left child
        # # trim the right subtree similarly by checking if any right child node
        # # is out of the [high, low] range
        # current = root
        # while current:
        #     # if the right child's value is greater than high, discard the right child
        #     while current.right and current.right.val > high:
        #         current.right = current.right.left  # move right pointer to the left child of the right node
        #     current = current.right  # move to the next right child
        # # return the adjusted root, which now represents the trimmed binary search tree
        # return root