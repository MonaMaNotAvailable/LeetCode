# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach 1: reverse the sub-level result before appending to the final output, time & space both O(n)
        # use a queue to keep track of nodes at the current level
        queue = deque([root])
        # output list to store the final zigzag level order traversal
        output = []
        # # Approach 2: variable to keep track of current depth
        # currentDepth = 0
        # # Approach 3: flag to determine the direction of zigzag traversal
        # leftToRight = True

        while queue:
            # get the number of nodes at the current level
            levelSize = len(queue)
            # temporary list to store the values of nodes at the current level
            temp = []
            for _ in range(levelSize):
                # pop the leftmost node from the queue
                node = queue.popleft()
                if node:
                    # add the node's value to the temporary list
                    temp.append(node.val)
                    # if the left child exists, add it to the queue
                    if node.left:
                        queue.append(node.left)
                    # if the right child exists, add it to the queue
                    if node.right:
                        queue.append(node.right)
            if temp:
                # if the current level is odd, reverse the temporary list
                if len(output) % 2 == 1:
                # # if the current depth is odd, instead of measuring the length each time
                # if currentDepth % 2 == 1:
                # if the current direction is right to left
                # if not leftToRight:
                    temp.reverse()
                # add the temporary list to the output list
                output.append(temp)
                # # toggle the direction for the next level
                # leftToRight = not leftToRight
            # # increment the current depth
            # currentDepth += 1
        # return the final zigzag level order traversal
        return output