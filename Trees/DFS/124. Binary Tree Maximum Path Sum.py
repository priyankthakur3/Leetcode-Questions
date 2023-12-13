# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs_helper(root, curr_sum):
            if not root:
                return 0

            left = dfs_helper(root.left, 0)
            right = dfs_helper(root.right, 0)
            
            self.res = max(self.res, root.val + left + right)
            return max(root.val, root.val + max(left, right), 0)

        dfs_helper(root,0)
        return self.res