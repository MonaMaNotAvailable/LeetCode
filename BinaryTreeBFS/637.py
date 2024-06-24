# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Approach 1: use deque & combine traversal and average calculation
        # time O(n), space O(max(w, h)) where w is the maximum width and h is the height of the tree
        queue = deque([root])
        output = []
        
        while queue:
            levelSum = 0
            levelCount = len(queue)
            # iterate over all nodes at the current level
            for _ in range(levelCount):
                node = queue.popleft() #removing an element from the front of a deque (popleft()) has an O(1) time complexity
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # calculate the average for the current level and add it to the output list
            output.append(levelSum / levelCount)
        return output



        # # Approach 2: use list & calculate at each level
        # # # time O(n^2), space O(max(w, h)) where w is the maximum width and h is the height of the tree
        # queue = [root]
        # output = []

        # while queue:
        #     n = len(queue)
        #     # calculate avg
        #     temp = 0
        #     for item in queue:
        #         temp += item.val
        #     output.append(temp/n)
        #     # accumulate the new level
        #     for _ in range(n):
        #         node = queue.pop(0) #removing an element from the front of a list (pop(0)) has an O(n) time complexity?!
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return output



        # # Approach 3: dfs & dictionary
        # # time O(n), space O(h) where h is the height of the tree
        # lvlcnt = defaultdict(int)
        # lvlsum = defaultdict(int)

        # def dfs(node: TreeNode, level: int) -> None:
        #     if not node:
        #         return
        #     lvlcnt[level] += 1
        #     lvlsum[level] += node.val
        #     dfs(node.left, level + 1)
        #     dfs(node.right, level + 1)
            
        # dfs(root, 0)
        # return [lvlsum[level] / lvlcnt[level] for level in range(len(lvlcnt))]