# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1 = []
        stack2 = []
        answer = []

        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            
            while root2:
                stack2.append(root2)
                root2 = root2.left
        
            if not stack2 or stack1 and stack2[-1].val >= stack1[-1].val:
                root1 = stack1.pop()
                answer.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                answer.append(root2.val)
                root2 = root2.right
        
        return answer
        # def inorder(r: TreeNode):
        #     return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        # return sorted(inorder(root1) + inorder(root2))
