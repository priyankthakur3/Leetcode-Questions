# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointer
# iterate till pointer are not same for the list
# if either pointer for linkedlist reaches end assign its pointer to head of another list
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while (pa != pb):
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa
