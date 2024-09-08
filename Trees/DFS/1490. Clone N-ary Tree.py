"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        clone = {None: None}

        def helper(root):

            if root in clone:
                return clone[root]
            
            new_root = Node(root.val)
            clone[root] = new_root
            for nei in root.children:
                new_root.children.append(helper(nei))
            return new_root
        
        return helper(root)
