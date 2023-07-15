# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        answer = []
        queue = collections.deque([root])

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()
                if not node:
                    answer.append('Null')
                else:
                    answer.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)

        return '/'.join(answer)        

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """


        tree = data.split('/')
        if tree[0] == 'Null':
            return None
            
        root = TreeNode(int(tree[0]))
        index = 1
        stack = [root]

        while stack:
            if tree[index] != 'Null':
                stack[0].left = TreeNode(int(tree[index]))
                index += 1
                stack.append(stack[0].left)
            else:
                stack[0].left = None
                index += 1
            if tree[index] != 'Null':
                stack[0].right = TreeNode(int(tree[index]))
                index += 1
                stack.append(stack[0].right)
            else:
                stack[0].right = None
                index += 1
            stack.pop(0)
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))