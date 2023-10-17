# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if at end of linked List return node
        if head is None or head.next is None:
            return head
        # pointer will not change
        reversed = self.reverseList(head.next)
        # point current node next node's next to current node
        head.next.next = head
        # remove link between current node and next node
        head.next = None
        return reversed
