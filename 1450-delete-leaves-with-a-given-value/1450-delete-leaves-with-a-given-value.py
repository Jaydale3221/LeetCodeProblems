# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        return self._helper(root, target)

    def _helper(self, node, target):
        if not node:
            return None
        
        node.left = self._helper(node.left, target)
        node.right = self._helper(node.right, target)

        if node.left==None and node.right==None and node.val==target:
            return None
        
        return node
