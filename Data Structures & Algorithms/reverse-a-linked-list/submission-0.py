# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        cur_node = head
        prev = None

        while cur_node:
            nxt_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt_node

        return prev