# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach1: Recursive DFS to find LCA (ChatGPT)
        def dfs(node: 'TreeNode'):
            if not node:
                return None
            # If the current node is either p or q, return the node
            if node == p or node == q:
                return node
            # Recursively find p and q in the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # If p and q found in different subtrees, node is the LCA (If both the left and right recursive calls return non-null results (left and right), it means that node p was found in one subtree (left or right) and node q in the other subtree. This makes the current node the lowest common ancestor of p and q, as it is the deepest node that has both p and q as descendants (one in each subtree).)
            if left and right:
                return node
            # Otherwise, return the non-null child (either left or right), handles the scenario where both p and q might be in the same subtree or if only one of the target nodes is present in the tree
            return left if left else right
        # Start the DFS from the root
        return dfs(root)



        # # Approach2: find 2 paths iteratively and compare for the 1st common node
        # def findPath(root: 'TreeNode', target: int) -> list:
        #     if root is None:
        #         return None
        #     # This dictionary will store the parent of each node
        #     parent = {root: None}
        #     stack = [root]
        #     while stack:
        #         node = stack.pop()
        #         # Process the node
        #         if node.val == target:
        #             # Reconstruct the path from node to root using the parent dictionary
        #             path = []
        #             while node:
        #                 path.append(node)
        #                 node = parent[node]
        #             return path
        #         if node.right:
        #             stack.append(node.right)
        #             parent[node.right] = node  # Set the parent of the right child
        #         if node.left:
        #             stack.append(node.left)
        #             parent[node.left] = node  # Set the parent of the left child
        #     return None  # Return None if the target is not found

        # def findFirstCommon(list1, list2) -> int:
        #     # print(list1)
        #     # print(list2)
        #     set1 = set(list1)  # Convert the first list to a set
        #     for node in list2:  # Iterate through the second list
        #         if node in set1:  # Check if the number is in the set
        #             return node  # Return the first common number
        #     return None  # If no common element is found
        
        # # find the dfs path for both p & q
        # listP = findPath(root, p.val)
        # listQ = findPath(root, q.val)
        # # compare the path 
        # return findFirstCommon(listP, listQ)



        # # Appraoch 3: super short but slower, always examines both the left and right children of every node, regardless of whether the LCA has already been identified in one subtree.
        # if not root or root == p or root == q:
        #     return root

        # l = self.lowestCommonAncestor(root.left, p, q)
        # r = self.lowestCommonAncestor(root.right, p, q)

        # if l and r:
        #     return root
        # return l or r