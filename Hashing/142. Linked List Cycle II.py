# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        curr = head 
        while curr:
            if curr in visited_nodes:
                return curr
            
            visited_nodes.add(curr)
            curr = curr.next
        
        return None