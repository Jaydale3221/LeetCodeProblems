# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = []
        maximum = float('-inf')
        level = 1


        while queue:
            length = len(queue)
            total_sum = 0
           
            for _ in range(length):
                node = queue.popleft()
                total_sum += node.val

                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if maximum < total_sum:
                maxlevel = level
                maximum = total_sum
            level += 1 
        
        return maxlevel
                

