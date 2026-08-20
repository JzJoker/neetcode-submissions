# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        while n:
            right = right.next
            n -= 1
        
        res = right1 = ListNode(None, head)
        while right:
            right = right.next
            right1 = right1.next
        
        right1.next = right1.next.next

        return res.next