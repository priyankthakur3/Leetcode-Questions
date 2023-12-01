"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edge case handle end nodes
        oldToNew = { None: None }
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        # 2nd pass set all pointers
        curr = head
        while curr:
            new_node_cur = oldToNew[curr]
            new_node_cur.next = oldToNew[curr.next]
            new_node_cur.random = oldToNew[curr.random]
            curr = curr.next
        # return new head node for new Node

        return oldToNew[head]