# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        target = []
        queue = deque()
        queue.append([root, targetSum, [root.val]])
        while queue:
            temp_node, local_sum, path = queue.popleft()
            local_sum -= temp_node.val

            if not temp_node.right and not temp_node.left and local_sum == 0:
                target.append(path)

            if temp_node.left:
                queue.append([temp_node.left, local_sum,
                             path + [temp_node.left.val]])

            if temp_node.right:
                queue.append([temp_node.right, local_sum,
                             path + [temp_node.right.val]])

        return target
