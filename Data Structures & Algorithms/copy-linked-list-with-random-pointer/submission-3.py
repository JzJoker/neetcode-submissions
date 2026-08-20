"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map_old_to_copy = {None : None}
        cur = head
        while cur:
            map_old_to_copy[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = map_old_to_copy[cur]
            copy.next = map_old_to_copy[cur.next]
            copy.random = map_old_to_copy[cur.random]
            cur = cur.next
        return map_old_to_copy[head]