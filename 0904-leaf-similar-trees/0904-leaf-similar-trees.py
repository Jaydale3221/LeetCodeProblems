# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            result = []
            if node:
                if not node.left and not node.right:
                    result.append(node.val)
                result.extend(dfs(node.left))
                result.extend(dfs(node.right))
            return result

        return dfs(root1) == dfs(root2)

     