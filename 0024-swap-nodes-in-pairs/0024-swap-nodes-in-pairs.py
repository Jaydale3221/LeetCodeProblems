# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        temp = dummy
        current = head

        while current and current.next:
            newPair = current.next.next
            second = current.next

            second.next  = current 
            current.next = newPair
            temp.next = second

            temp = current
            current  = newPair
        
        return dummy.next

