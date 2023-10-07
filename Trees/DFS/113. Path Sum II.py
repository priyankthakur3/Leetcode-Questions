# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []
        self.target = []
        self.helper(root, targetSum, [])
        return self.target

    def helper(self, root, local_sum, path):
        if not root:
            return

        local_sum -= root.val
        path.append(root.val)
        if not root.left and not root.right and local_sum == 0:
            self.target.append(path[::])

        if root.left:
            self.helper(root.left, local_sum, path)

        if root.right:
            self.helper(root.right, local_sum, path)

        path.pop(-1)
