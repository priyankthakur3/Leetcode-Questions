# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        res = set([root])

        def dfs(root):

            if not root:
                return None
            
            node = root
            if root.val in to_delete:
                root = None
                res.discard(node)
                if node.left:
                    res.add(node.left)
                if node.right:
                    res.add(node.right)
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return root
        
        dfs(root)
        return list(res)
