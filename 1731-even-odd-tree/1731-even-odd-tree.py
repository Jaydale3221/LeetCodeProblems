# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0

        while queue:
            length = len(queue)

            if level % 2 == 0:
                previous = float('-inf')

                for _ in range(length):
                    node = queue.popleft()
                
                    if node.val % 2 == 0: return False
                    elif previous >= node.val: return False
                    previous = node.val

                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

            else:
                previous = float('inf')
                for _ in range(length):
                    node = queue.popleft()

                    if node.val % 2 == 1: return False
                    elif previous <= node.val: return False
                    previous = node.val

                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            
            level += 1
        return True

