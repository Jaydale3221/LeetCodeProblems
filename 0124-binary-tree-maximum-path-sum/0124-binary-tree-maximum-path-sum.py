# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maximumSum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def calculateGain(root):
            if not root: return 0
            
            leftGain = max(0,calculateGain(root.left))
            rightGain = max(0,calculateGain(root.right))


            self.maximumSum = max(self.maximumSum, rightGain + leftGain + root.val)

            return max(rightGain + root.val, leftGain + root.val)

        calculateGain(root)

        return self.maximumSum
