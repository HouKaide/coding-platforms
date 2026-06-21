from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        initial_node = ListNode()
        previous_node = initial_node
        carry_on = 0
        while (l1 or l2) or (carry_on > 0):
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry_on
            carry_on = int(val / 10.0) if val > 0 else 0
            previous_node.next = ListNode(val=int(val % 10))
            previous_node = previous_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return initial_node.next
