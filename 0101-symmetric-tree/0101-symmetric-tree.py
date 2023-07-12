# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isTreeSymmetric(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True #Edgecase

        if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
            return False #Edgecase

        if leftRoot.val != rightRoot.val:
            return False #Edgecase
         
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left) # left and right node and compare values

    def isSymmetric(self,root): #Function 
        return self.isTreeSymmetric(root.left, root.right)
        
  