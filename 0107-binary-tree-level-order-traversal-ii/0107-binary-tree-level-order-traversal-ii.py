# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []
        if not root: return []

        while queue:
            length = len(queue)
            current = []

            for _ in range(length):
                node = queue.popleft()
                current.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(current)
        result.reverse()

        return result 