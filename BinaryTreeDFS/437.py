# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Appriach1: use dict & dfs
        # initialize a dictionary
        pathsCount = defaultdict(int)
        # Initialize with base case: one way to get sum = 0 by not taking any node
        pathsCount[0] = 1
    
        # traverse each node of the tree
        def dfs(n:TreeNode, preValue:int) -> int:
            if not n:
                return 0
            print(n.val, preValue)
            # current path sum including this node
            preValue += n.val
            # record in a dict
            pathCount = pathsCount[preValue - targetSum]
            # update the paths count
            pathsCount[preValue] += 1
            # traverse to left and right child
            output = pathCount + dfs(n.left, preValue) + dfs(n.right, preValue)
            #backtrack
            pathsCount[preValue] -= 1
            return output

        return dfs(root, 0)