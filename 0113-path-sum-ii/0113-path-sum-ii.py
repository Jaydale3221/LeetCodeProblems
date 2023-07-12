# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
      
        def dfs(node, path_sum, path):
            if not node:
                return

            path_sum += node.val
            path.append(node.val)

            if not node.left and not node.right and path_sum == targetSum:
                res.append(path)         
            
            dfs(node.left, path_sum, path[:])
            # print(path)
            dfs(node.right, path_sum, path[:])

        dfs(root, 0, [])
        return res
            