# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        flag = True

        queue = deque()
        queue.append([root.left,root.right])
        while queue:
            left, right = queue.popleft()

            # leaf node
            if left is None and right is None:
                continue

            # imbalanced node either left or right missing or value are not equal
            if (left is None or right is None) or left.val != right.val:
                return False
            
            queue.append([left.left,right.right])
            queue.append([left.right,right.left])
        
        return True
                
        