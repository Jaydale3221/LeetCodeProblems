# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        answer = float("inf")


        def dfs(node):
            if not node: return

            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)

        dfs(root)


        for i in range(1, len(values)):
            answer = min(answer, values[i] - values[i - 1])
        
        return answer
