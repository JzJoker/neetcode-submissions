# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for head in lists:
            while head:
                nums.append(head.val)
                head = head.next
        nums.sort()
        res = dummy = ListNode()
        for num in nums:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return res.next