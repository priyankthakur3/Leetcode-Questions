# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = collections.deque()
        queue.append([root, root.val])
        while queue:
            node, local_max = queue.popleft()
            if node:
                if node.val >= local_max:
                    local_max = node.val
                    res += 1
                queue.append([node.left, local_max])
                queue.append([node.right, local_max])        
        return res