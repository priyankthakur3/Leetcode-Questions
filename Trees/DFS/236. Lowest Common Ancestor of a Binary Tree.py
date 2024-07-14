# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, left, right):

            if not root:
                return None
            
            if root.val == p.val or root.val == q.val:
                return root
            
            left = helper(root.left, left , right)
            right = helper(root.right, left , right)

            if left and right:
                return root
            
            if left:
                return left
            
            return right
        
        return helper(root, p, q)