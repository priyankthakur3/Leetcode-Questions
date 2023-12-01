# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def helper(left, right):
            dummy = ListNode(-1)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = ListNode(left.val)
                    left = left.next
                else:
                    curr.next = ListNode(right.val)
                    right = right.next

                curr = curr.next
            if left != None:
                curr.next = left
            if right!= None:
                curr.next = right
            return dummy.next
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []
            for i in range(0,len(lists),2):
                l1 = lists[i] 
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergeList.append(helper(l1,l2))
            lists = mergeList
        return lists[0]