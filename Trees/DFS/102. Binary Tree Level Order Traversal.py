# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.dfs_helper(root, 0)
        return self.result

    def dfs_helper(self, root, level):
        if not root:
            return
        if level > len(self.result) - 1:
            self.result.append([root.val])

        else:
            self.result[level].append(root.val)

        self.dfs_helper(root.left, level + 1)
        self.dfs_helper(root.right, level + 1)
