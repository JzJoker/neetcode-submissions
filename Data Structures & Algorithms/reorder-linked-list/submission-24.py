# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        cur = slow.next
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # merge
        list1, list2 = head, prev
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1, list2 = tmp1, tmp2