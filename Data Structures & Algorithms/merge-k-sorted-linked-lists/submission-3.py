# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(float('-inf'))
        for l in lists:
            res = self.mergeLists(res, l)
        return res.next

    def mergeLists(self, list1, list2):
        res = dummy = ListNode()    
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return res.next