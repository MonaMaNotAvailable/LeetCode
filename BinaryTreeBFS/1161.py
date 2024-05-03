# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Approach 1: bfs & compute sum per level
        queue = [root]
        maxSum = root.val
        currentLevel = 1
        output = 1

        while queue:
            n = len(queue) #only process the nodes on the same level
            currentSum = 0
            for i in range(n):
                node = queue.pop(0)
                # calculate sum
                currentSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # for node in queue: #validate node on the same level
            #     print(node.val)

            # find current max & record level
            if maxSum < currentSum:
                maxSum = currentSum
                output = currentLevel

            # increment level
            currentLevel += 1
        return output

        # # Approach 2: dfs & dictionary
        # levels = defaultdict(int)
        # def dfs(root, depth):
        #     if root:
        #         levels[depth] += root.val
        #         dfs(root.left,  depth+1)
        #         dfs(root.right, depth+1)
			
        # dfs(root, 1)
        # return max(levels, key=levels.get)