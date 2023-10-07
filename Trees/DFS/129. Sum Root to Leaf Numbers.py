# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# pre-order traversal
class Solution:
    numbers_list = []
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)

    def helper(self,root,local):
        if root is None:
            return 0
        local = local * 10 + root.val
        if root.left == None and root.right == None:
            return local
        return self.helper(root.left,local) + self.helper(root.right,local)