# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach 1: recursive in-order traversal with single variable, time O(n), space O(h) where h is the max height of the bst
        self.count = 0  # initialize count to keep track of the number of nodes visited
        self.result = None  # initialize result to store the k-th smallest element
        def traverse(node):
            if not node or self.result is not None:  # base case: if node is None or result is already found, return
                return
            traverse(node.left)  # recursively traverse the left subtree
            self.count += 1  # increment count when a node is visited
            if self.count == k:  # check if count equals k
                self.result = node.val  # if true, store the node's value in result
                return  # terminate further recursion as the k-th smallest element is found
            traverse(node.right)  # recursively traverse the right subtree
        traverse(root)  # start the traversal from the root
        return self.result  # return the k-th smallest element



        # Approach 2: recursive in-order traversal with ordered list, time O(n), space O(n)
        result = []
        def traverse(node):
            if node and len(result) < k:
                traverse(node.left)      # visit left subtree
                result.append(node.val)  # append current node val
                traverse(node.right)     # visit right subtree
        traverse(root)
        return result[k-1]



        # Approach 3: iterative backtrack in-order traversal, time O(n), space O(h)
        stack = []  # initialize an empty stack to help with the traversal
        curr = root  # start the traversal from the root of the bst
        while stack or curr:  # continue as long as there are nodes to process (either in the stack or current node is not none)
            while curr:  # traverse to the leftmost node of the current subtree
                stack.append(curr)  # push the current node onto the stack
                curr = curr.left  # move to the left child of the current node
            curr = stack.pop()  # pop the node from the stack (backtrack to the last node with an unexplored right child)
            k -= 1  # decrement k because one more node has been visited
            if k == 0:  # if k is now zero, we have found the k-th smallest element
                return curr.val  # return the value of the current node
            curr = curr.right  # move to the right child of the current node to continue the in-order traversal