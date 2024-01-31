# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        # push initial linkedlist header node in heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i, lists[i]))
        new_list = ListNode(-1)
        dummy = new_list
        while heap:
            # get initially inserted node pointer, its value and index
            node_val, idx, node_ptr = heapq.heappop(heap)
            dummy.next = ListNode(node_val)
            dummy = dummy.next
            # shift pointer to next element
            if node_ptr.next:
                heapq.heappush(heap,(node_ptr.next.val, idx, node_ptr.next))
        return new_list.next
