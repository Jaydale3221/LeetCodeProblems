"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        queue = deque([root])

        while queue:
            length = len(queue)
            

            for i in range(length):
                node = queue.popleft()

                if i < length -1:
                    node.next = queue[0]
                    # print(queue[0])

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root





        # if not root:
        #     return root
        # q = []
        
        # q.append(root)
        
        # tail = root
        # while len(q) > 0:
        #     node = q.pop(0)
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
                
        #     if node == tail:
        #         node.next = None
        #         tail = q[-1] if len(q) > 0 else None
        #     else:
        #         node.next = q[0]
                
        # return root
         