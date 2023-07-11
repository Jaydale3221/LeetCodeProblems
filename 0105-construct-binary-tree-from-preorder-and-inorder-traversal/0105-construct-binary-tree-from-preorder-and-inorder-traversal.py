# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


        
        # if not preorder or not inorder: return None
        
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])


        # root.left = self.buildTree(preorder[1:mid +1 ], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # return root


        # def array_to_tree(left, right):


            # nonlocal preorder_index
        #     # if there are no elements to construct the tree
        #     if left > right: return None

        #     # select the preorder_index element as the root and increment it
        #     root_value = preorder[preorder_index]
        #     root = TreeNode(root_value) # TREE NODE ASSIGNED


        #     preorder_index += 1

        #     # build left and right subtree
        #     # excluding inorder_index_map[root_value] element because it's the root
        #     root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
        #     root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

        #     return root

        # preorder_index = 0

        # # build a hashmap to store value -> its index relations
        # inorder_index_map = {}
        # for index, value in enumerate(inorder):
        #     inorder_index_map[value] = index

        # return array_to_tree(0, len(preorder) - 1)
