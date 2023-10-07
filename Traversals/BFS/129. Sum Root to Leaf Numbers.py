# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()

        total_sum = 0
        queue.append([root, 0])
        while queue:
            temp_node, local = queue.popleft()
            local = local * 10 + temp_node.val
            if not temp_node.left and not temp_node.right:
                total_sum += local
            if temp_node.left:
                queue.append([temp_node.left, local])
            if temp_node.right:
                queue.append([temp_node.right, local])
        return total_sum
