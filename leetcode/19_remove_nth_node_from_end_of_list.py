from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        delayed_head = head
        original_head = delayed_head
        size = n
        length = 0
        if n == 1 and head and not head.next:
            return None
        while head:
            if n == -1:
                delayed_head = delayed_head.next
            else:
                n = n - 1
            head = head.next
            length += 1
        if length == size and original_head and original_head.next:
            return original_head.next
        if size > 1:
            delayed_head.next = delayed_head.next.next if size > 1 else None
        elif size == 1:
            delayed_head.next = None
        return original_head




