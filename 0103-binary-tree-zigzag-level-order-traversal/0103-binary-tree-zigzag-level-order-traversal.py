# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level = 0
        result = []
        queue = deque([root])

        while queue:
            length = len(queue)
            current_level = []

            for _ in range(length):
                node = queue.popleft()

                if level % 2 == 0:
                    current_level.append(node.val)
                else:
                    current_level.insert(0, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            level += 1
        return result