# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        slow, second = head, prev
        while second:
            temp1, temp2 = slow.next, second.next
            slow.next = second
            second.next = temp1
            slow, second = temp1, temp2
