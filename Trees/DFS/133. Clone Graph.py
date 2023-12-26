"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        
        def helper(node):
            if node in mapping:
                return mapping[node]

            copy = Node(node.val)
            mapping[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(helper(nei))
            return copy

        return helper(node) if node else None            