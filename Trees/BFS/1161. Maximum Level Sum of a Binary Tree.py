# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        lvl_max = 0
        max_lvl_sum = float('-inf')
        lvl = 1
        while queue:
            lvl_sum = 0
            q_len = len(queue)
            for _ in range(q_len):
                t_node = queue.popleft()
                lvl_sum += t_node.val
                if t_node.left:
                    queue.append(t_node.left)
                if t_node.right:
                    queue.append(t_node.right)
            if lvl_sum > max_lvl_sum:
                max_lvl_sum = lvl_sum
                lvl_max = lvl
            lvl += 1

        return lvl_max