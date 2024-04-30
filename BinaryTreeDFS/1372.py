# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.maxLength = 0

        #Approach 1: Check left/right node exists first, then check next direction
        def solve(n, depth, direction):
            self.maxLength = max(self.maxLength, depth)

            if n.left:
                if direction == 'left':
                    solve(n.left, 1, 'left')
                else:
                    solve(n.left, depth+1, 'left')
            if n.right:
                if direction == 'right':
                    solve(n.right, 1, 'right')
                else:
                    solve(n.right, depth+1, 'right')

        solve(root, 0, '')
        # # Approach 2: Super slow, using dfs, direction in the parameters & keep track of max length so far
        # #left -1, right is +1
        # def dfs(n:TreeNode, currentDirection:int, currentLength:int):
        #     if n is None:
        #         return 

        #     # Update the maximum length found so far
        #     self.maxLength = max(self.maxLength, currentLength)
        #     print(self.maxLength)

        #     if currentDirection == -1 or currentDirection == 0: #previously went left
        #         if n.right: # continue to go to right
        #             dfs(n.right, 1, currentLength + 1)
        #         if n.left: # new path to left
        #             dfs(n.left, -1, 1)
        #     if currentDirection == 1 or currentDirection == 0: #previoudly went right
        #         if n.left: # continue to go to left
        #             dfs(n.left, -1, currentLength+1)
        #         if n.right: # new path to right
        #             dfs(n.right, 1, 1)
        
        # dfs(root, 0, 0)
        
        return self.maxLength