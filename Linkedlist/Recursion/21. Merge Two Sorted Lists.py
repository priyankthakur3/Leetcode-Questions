# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        self.dummy = ListNode()
        self.temp = self.dummy

        def helper(list1, list2):
            if not list1:
                self.temp.next = list2
                return
            if not list2:
                self.temp.next = list1
                return
            
            if list1.val < list2.val:
                self.temp.next = list1
                self.temp = self.temp.next
                helper(list1.next, list2)
            else:
                self.temp.next = list2
                self.temp = self.temp.next
                helper(list1, list2.next)
            
        helper(list1, list2)
        return self.dummy.next