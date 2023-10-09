# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        self.flag = True

        def dfs_helper(left, right):

            if left is None and right is None:
                return
            if (left is None or right is None) or left.val != right.val:
                self.flag = False

            if self.flag:
                dfs_helper(left.left, right.right)
            if self.flag:
                dfs_helper(left.right, right.left)

        dfs_helper(root.left, root.right)
        return self.flag
