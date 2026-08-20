# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        
        # reverse second half
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # merge alternating
        first = head
        while prev:
            tmp1 = first.next
            tmp2 = prev.next
            first.next = prev
            prev.next = tmp1
            first = tmp1
            prev = tmp2          
