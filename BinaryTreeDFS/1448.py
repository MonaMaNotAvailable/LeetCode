# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
    # Approach 1: Recursive & without using max
        def dfs(node, prev_val):
            if not node:
                return 0
            elif node.val >= prev_val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, prev_val) + dfs(node.right, prev_val)

        return dfs(root, root.val)



    # # Approach2: Stack
    # def goodNodes(self, root: TreeNode) -> int:
    #     stack = [(root,float('-inf'))]
    #     count = 0
    #     while stack:
    #         node, maxNum = stack.pop()
    #         if node.val>=maxNum:
    #             count+=1
    #         maxNum = max(maxNum,node.val)
    #         if node.left:
    #             stack.append((node.left,maxNum))
    #         if node.right:
    #             stack.append((node.right,maxNum))
    #     return count



    # # Approach3: Recursive & too slow
    # def __init__(self):
    #     self.count = 0  # Initialize the count here to reset for each instance
    
    # def dfs(self, tree, currentMax):
    #     if tree is None:
    #         return  # Base case: index out of bounds or null node
        
    #     if tree.val >= currentMax:
    #         self.count += 1  # Increment the count if it's a "good node"
        
    #     # Print statements for debugging (you can comment these out in your final submission)
    #     print(f"Current Node: {tree.val}, Current Max: {currentMax}, Good Nodes Count: {self.count}")
        
    #     # Update the current max to pass to children
    #     newMax = max(currentMax, tree.val)
        
    #     # Recursive DFS on the left and right children
    #     self.dfs(tree.left, newMax)
    #     self.dfs(tree.right, newMax)
    
    # def goodNodes(self, root: TreeNode) -> int:
    #     self.count = 0  # Reset count for each function call
    #     self.dfs(root, float('-inf'))  # Use negative infinity to handle any tree value
    #     return self.count