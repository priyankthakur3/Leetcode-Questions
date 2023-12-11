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

        self.res = 0
        def dfs_helper(root, max_val):
            if not root:
                return
            
            if root.val >= max_val:
                max_val = root.val
                self.res += 1
            
            if root.left:
                dfs_helper(root.left, max_val )
            
            if root.right:
                dfs_helper(root.right, max_val )
        
        dfs_helper(root, root.val)
        return self.res