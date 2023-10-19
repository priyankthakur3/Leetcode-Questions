# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        lparent, llevel = self.__dfs_helper(root, 0, None, x)
        rparent, rlevel = self.__dfs_helper(root, 0, None, y)

        return lparent != rparent and llevel == rlevel

    def __dfs_helper(self, root, level, parent, target):

        if not root:
            return []
        if root:
            if root.val == target:
                return parent, level

        return self.__dfs_helper(root.left, level + 1, root, target) or self.__dfs_helper(root.right, level + 1, root, target)
