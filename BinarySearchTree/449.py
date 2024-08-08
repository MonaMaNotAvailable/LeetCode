# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Approach 1: bfs, all 3 approaches have time & space O(n)
    def serialize(self, root: Optional[TreeNode]) -> str:
        """encodes a tree to a single string."""
        if not root:
            return "#"
        # initialize a queue for BFS
        queue = deque([root])
        output = []
        # perform BFS
        while queue:
            node = queue.popleft()
            if node:
                # append the node value to the output list
                output.append(str(node.val))
                # enqueue left and right children
                queue.append(node.left)
                queue.append(node.right)
            else:
                # append a marker for a None node
                output.append("#")
        # join the output list with '/' to form the serialized string
        return "/".join(output)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """decodes your encoded data to tree."""
        if data == "#":
            return None
        # split the serialized string to get the node values
        nodes = data.split('/')
        # create the root node with the first value
        root = TreeNode(int(nodes[0]))
        # initialize a queue for BFS
        queue = deque([root])
        index = 1
        # perform BFS to reconstruct the tree
        while queue:
            node = queue.popleft()
            # process the left child
            if nodes[index] != "#":
                left_child = TreeNode(int(nodes[index]))
                node.left = left_child
                queue.append(left_child)
            index += 1
            # process the right child
            if nodes[index] != "#":
                right_child = TreeNode(int(nodes[index]))
                node.right = right_child
                queue.append(right_child)
            index += 1
        return root



    # # Approach 2: dfs pre-order
    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     """Encodes a tree to a single string."""
    #     output = []
        
    #     def dfsPreOrder(node):
    #         if node:
    #             # visit the node
    #             output.append(str(node.val))
    #             # traverse the left subtree
    #             dfsPreOrder(node.left)
    #             # traverse the right subtree
    #             dfsPreOrder(node.right)
        
    #     dfsPreOrder(root)
    #     return "/".join(output)

    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     """Decodes your encoded data to tree."""
    #     if not data:
    #         return None
    #     # parse the string and convert it to a list of integers
    #     vals = [int(x) for x in data.split('/')]
        
    #     def buildTree(lower, upper):
    #         # check if there are values left and the current value fits the BST property
    #         if vals and lower < vals[0] < upper:
    #             # pop the first value
    #             val = vals.pop(0)
    #             # create a new node with the popped value
    #             root = TreeNode(val)
    #             # recursively build the left subtree with updated upper bound
    #             root.left = buildTree(lower, val)
    #             # recursively build the right subtree with updated lower bound
    #             root.right = buildTree(val, upper)
    #             return root
    #         # return None if no valid node can be created
    #         return None
        
    #     # start building the tree with initial bounds
    #     return buildTree(float('-inf'), float('inf'))



    # # Approach 3: in-order traversal loses the structure of the original tree, 
    # # making it impossible to reconstruct the tree accurately (e.g. [2,1,3] and [3,2,1] both become [1,2,3])
    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     """Encodes a tree to a single string.
    #     """
    #     output = []
        
    #     def dfsInOrder(node):
    #         if node:
    #             # traverse the left subtree
    #             dfsInOrder(node.left)
    #             # visit the node
    #             output.append(str(node.val))
    #             # traverse the right subtree
    #             dfsInOrder(node.right)
    #     dfsInOrder(root)
    #     # print("/".join(output))
    #     return "/".join(output)

    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     """Decodes your encoded data to tree.
    #     """
    #     def sortedListToBst(nums):
    #         if not nums:
    #             return None
    #         # find the middle index
    #         mid = len(nums) // 2
    #         # create a new node with the middle element
    #         root = TreeNode(nums[mid])
    #         # recursively build the left subtree with the left half of the list
    #         root.left = sortedListToBst(nums[:mid])
    #         # recursively build the right subtree with the right half of the list
    #         root.right = sortedListToBst(nums[mid + 1:])
    #         return root

    #     # parse the string and convert it to a list of integers
    #     parsedString = [int(x) for x in data.split('/') if x]
    #     return sortedListToBst(parsedString)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans