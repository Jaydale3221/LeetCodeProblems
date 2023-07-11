# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res=[]
        def inorder(root):
            if root is None:
                return 

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

            return res

        values=inorder(root)
        # values.sort()
        return values[k-1]



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
        