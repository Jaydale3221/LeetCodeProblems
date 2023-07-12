# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, num):
            if node is None: return 0
        # do calculations       
            num = num * 10 + node.val

        #base case
            if not node.left and  not node.right: return num
                
        # do same for left and right side using recursion
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root,0)

                