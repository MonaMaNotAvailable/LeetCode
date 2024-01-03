# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #faster
    def _dfs(self, root: Optional[TreeNode], cur, res) -> None:
        # Base Case
        if not root:
            return
        
        # Append node to path
        cur.append(str(root.val))
        
        # If root is a leaf, append path to result
        if not root.left and not root.right:
            res.append('->'.join(cur))
            
        # Recursive Step
        self._dfs(root.left, cur, res)
        self._dfs(root.right, cur, res)
        
        # Backtracking / Post-processing / pop node from path
        cur.pop()
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self._dfs(root, [], res)
        return res

    #My solution: forgot to write printLeaf as a sub function within binaryTreePaths...
    # results = []
    # def printLeaf(self, path, node):
    #     if path:
    #         path += "->"
    #     path += str(node.val)
    #     #basecase
    #     if node.left==None and node.right==None:
    #         # path = "->".join(path)
    #         self.results.append(path)
    #         return
    #     #left not null
    #     if node.left!=None:
    #         self.printLeaf(path, node.left)
    #     #right not null
    #     if node.right!=None:
    #         self.printLeaf(path, node.right)
    
    # def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    #     self.results.clear()
    #     self.printLeaf("",root)
    #     print(self.results)
    #     return self.results