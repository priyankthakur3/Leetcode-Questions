# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        res = []
        queue.append([root, 0])
        while queue:
            quelen = len(queue)
            res_level = []
            for _ in range(quelen):
                node, level = queue.popleft()
                res_level.append(node.val)
                if node.left:
                    queue.append([node.left, level + 1])
                if node.right:
                    queue.append([node.right, level + 1])
            if level % 2 != 0:
                res.append(res_level[::-1])
            else:
                res.append(res_level)    
        return  res