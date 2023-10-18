# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        result = []

        def dfs_helper(root, level):
            # base case
            if not root:
                return
            # check if level increased if yes then append
            if level >= len(result):
                result.append(root.val)

            dfs_helper(root.right, level + 1)
            if root.left:
                dfs_helper(root.left, level + 1)

        dfs_helper(root, 0)
        return result
