# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Approach 1: inorder traversal to visit node in increasing order & calculate diff in-place
        # time O(n) and space O(h), where h is the height of the tree due to the recursion stack during traversal
        self.prev = -float('inf')  # initialize previous node value to negative infinity
        self.minDiff = float('inf')  # initialize minimum difference to positive infinity
        
        def inorder(node: Optional[TreeNode]):
            # base case: if node is None, return immediately
            if not node:
                return  
            inorder(node.left)  # recurse on the left child
            # update minDiff with the difference between current node value and previous node value
            self.minDiff = min(self.minDiff, node.val - self.prev)
            self.prev = node.val  # update prev to the current node's value
            inorder(node.right)  # recurse on the right child
        
        inorder(root)  # start the in-order traversal from the root
        return self.minDiff  # return the minimum difference found



        # # Approach 2: store every visited num in increasing order, time O(n) and space O(n)
        # tempList = []
        # # tree traversal
        # def treeTraversal(root: Optional[TreeNode]):
        #     if root:
        #         treeTraversal(root.left)
        #         tempList.append(root.val)
        #         treeTraversal(root.right)

        # treeTraversal(root)
        # output = float('inf')
        # # compare each consecutive pair
        # for i in range(1,len(tempList)):
        #     output = min(output, tempList[i]-tempList[i-1])
        # return output