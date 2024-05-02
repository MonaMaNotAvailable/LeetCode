# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach 1: bfs find the right most node per level & without expicit depth tracking
        result = []  # Initialize an empty list to store the rightmost values
        q = collections.deque([root])  # Initialize a deque with the root node
        
        # Perform BFS traversal
        while q:
            rightMost = None  # Initialize a variable to track the rightmost node at each level
            n = len(q)  # Get the number of nodes at the current level
            
            # Iterate through each node at the current level
            for i in range(n):
                node = q.popleft()  # Dequeue a node from the left of the deque
                if node:
                    rightMost = node  # Update the rightmost node
                    q.append(node.left)  # Enqueue the left child
                    q.append(node.right)  # Enqueue the right child
            
            # If a rightmost node was encountered at the current level, append its value to the result
            if rightMost:
                result.append(rightMost.val)
        
        return result  # Return the list containing the rightmost values



        # # Approach 2: dfs & recursively taking one node per level
        # res = []
        # def dfs(root, lvl):
        #     # if current node exist
        # 	if root:
        #         # only the first node encountered at each level (from right to left) is added to res
        # 		if len(res) == lvl:
        # 			res.append(root.val)
        #         # traverse the right and left child of the current node
        # 		dfs(root.right, lvl + 1)
        # 		dfs(root.left, lvl + 1)
        # 	return 
        # dfs(root,0)
        # return res



        # # Approach 3: bfs find the right most node per level using dict & tuple
        # if root is None:
        #     return []
        # queue = [(root, 0)]  # tuple: node and depth
        # result = {}

        # while queue:
        #     currentNode, depth = queue.pop(0)
        #     # Initialize a list of values per depth
        #     if depth not in result:
        #         result[depth] = []
        #     # Add to dict
        #     result[depth].append(currentNode.val)
        #     # Add the child nodes to the queue with incremented depth
        #     if currentNode.right:
        #         queue.append((currentNode.right, depth + 1))
        #     if currentNode.left:
        #         queue.append((currentNode.left, depth + 1))
        
        # # Get the right most value per depth
        # rightMost = []
        # for depth, values in result.items():
        #     rightMost.append(values[0])
            
        # return rightMost




        # Reusable bfs algo
        # def bfs(root: Optional[TreeNode]) -> List[int]:

        #     if root is None:
        #         return []
        #     queue = [root]
        #     result = []

        #     while queue:
        #         currentNode = queue.pop(0)
        #         result.append(currentNode.val)
        #         if currentNode.left:
        #             queue.append(currentNode.left)
        #         if currentNode.right:
        #             queue.append(currentNode.right)
        #         print(queue)
            
        #     return result
        
        # return bfs(root)     