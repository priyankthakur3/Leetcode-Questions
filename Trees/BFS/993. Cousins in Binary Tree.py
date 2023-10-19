# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        queue = collections.deque()
        queue.append([root, None, 0])
        lparent, rparent = None, None
        while queue:
            for _ in range(len(queue)):
                temp, parent, level = queue.popleft()
                if temp.val == x:
                    lparent, llevel = parent, level

                if temp.val == y:
                    rparent, rlevel = parent, level

                if temp.left:
                    queue.append([temp.left, temp.val, level + 1])
                if temp.right:
                    queue.append([temp.right, temp.val, level + 1])

                if rparent and lparent:
                    break

        return rparent != lparent and llevel == rlevel
