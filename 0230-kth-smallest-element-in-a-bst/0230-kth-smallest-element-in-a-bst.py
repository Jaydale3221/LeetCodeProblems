# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(node):
            if not node: return []

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

            return result

        values = inorder(root)
        return result[k-1]
 



        # n = 0 
        # stack = []

        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     n += 1

        #     if n == k:
        #         return curr.val
        #     curr  = curr.right
        