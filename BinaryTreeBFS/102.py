# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach 1: bfs with queue, time & space O(n) for both approaches
        if not root: 
            return []
        output = []  # list to hold the final result
        queue = deque([root])  # initialize the queue with the root node
        while queue:  # while there are nodes to process in the queue
            temp = []  # list to hold values of the current level
            for _ in range(len(queue)):  # iterate through the nodes at the current level
                node = queue.popleft()  # pop a node from the left of the queue
                temp.append(node.val)  # add the node's value to the current level list
                if node.left:  # if the left child exists
                    queue.append(node.left)  # add the left child to the queue
                if node.right:  # if the right child exists
                    queue.append(node.right)  # add the right child to the queue
            output.append(temp)  # add the current level list to the final result
        return output  # return the final result containing level order traversal of the tree



        # # Approach 2: dfs
        # ans = []  # list to hold the values of nodes at each level
        # def dfs(node, depth):
        #     if not node:  # if the node is None, return immediately
        #         return 
        #     if len(ans) <= depth:  # if we have reached a new level
        #         ans.append([node.val])  # add a new list for this level
        #     else:
        #         ans[depth].append(node.val)  # append the node's value to the existing level list
        #     dfs(node.left, depth + 1)  # recursively call dfs for the left child
        #     dfs(node.right, depth + 1)  # recursively call dfs for the right child
        # dfs(root, 0)  # start the dfs traversal from the root at depth 0
        # return ans  # return the final list of level order traversal