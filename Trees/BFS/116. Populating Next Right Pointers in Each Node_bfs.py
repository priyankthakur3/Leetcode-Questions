"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        queue = deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            right_node = None
            for _ in range(qlen):
                temp_node = queue.popleft()
                temp_node.next = right_node
                right_node = temp_node
                if temp_node.right:
                    queue.append(temp_node.right)
                if temp_node.left:
                    queue.append(temp_node.left)

        return root
        