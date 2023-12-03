# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append([root, 0])
        depth = 0
        while queue:
            elm , t_depth = queue.popleft()
            depth = max(depth, t_depth + 1)
            if elm.left:
                queue.append([elm.left, t_depth + 1])
            if elm.right:
                queue.append([elm.right, t_depth + 1])
        return depth