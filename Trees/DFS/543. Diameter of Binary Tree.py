# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def dfs_helper(root):

            if not root:
                return -1
            
            left = dfs_helper(root.left)
            right = dfs_helper(root.right)

            self.diameter = max(self.diameter, left + right + 2)

            return 1+ max(left, right) 
        dfs_helper(root)
        return self.diameter