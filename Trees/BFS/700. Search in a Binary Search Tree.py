# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)

        while queue:
            temp = queue.popleft()
            if temp.val == val:
                return temp
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        
        return None