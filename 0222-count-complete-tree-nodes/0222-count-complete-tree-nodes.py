# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 

        def leftDepth(node):
            if not node:
                return 0
            return 1 + leftDepth(node.left)
        
        def rightDepth(node):
            if not node:
                return 0
            return 1 + rightDepth(node.right)
        
        l, r = leftDepth(root), rightDepth(root)

        if l == r:
            return(2 ** l) - 1 
        
        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)