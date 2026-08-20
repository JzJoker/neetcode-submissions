class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = dummy = ListNode(0, head)
        group = head

        while True:
            kth = group
            count = 1
            while kth and count < k:
                kth = kth.next
                count += 1

            if not kth:
                dummy.next = group
                return res.next
                
            nxt = kth.next
            kth.next = None
            dummy.next = self.reverseLinkedList(group)
            dummy = group
            group = nxt

    def reverseLinkedList(self, head):
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev