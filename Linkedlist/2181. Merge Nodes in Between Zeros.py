# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)

        while head and head.next:
            prev.next = ListNode(head.val)
            head = head.next
            prev = prev.next
            while head and head.val != 0:
                prev.val += head.val
                head = head.next
            
        return dummy.next