# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot : return True 
        if not root : return False #order matter

        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and 
            self.sameTree(root.right, subRoot.right))
        
        return False #one tree is empty 
         
        # def dfs(node):
        #     if node is None:
        #         return False

        #     elif is_identical(node, subRoot):
        #         return True
        #     else: return dfs(node.left) or dfs(node.right)

        # def is_identical(node1, node2):
        #     if node1 is None or node2 is None:
        #         return node1 is None and node2 is None
        #     else:
        #         return (node1.val == node2.val and
        #                 is_identical(node1.left, node2.left) and
        #                 is_identical(node1.right, node2.right))

        # return dfs(root)