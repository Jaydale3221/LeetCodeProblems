# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def helper(root, sum):
            if not root: return 0
            result = 0

            if root.val == sum: result += 1
            result += helper(root.left, sum - root.val)
            result += helper(root.right, sum - root.val)
            
            return result


        if not root: return 0
        return self.pathSum(root.left ,sum) + helper(root, sum) + self.pathSum(root.right, sum)

