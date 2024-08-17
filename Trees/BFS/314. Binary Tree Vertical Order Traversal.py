# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        queue = deque()
        queue.append([root, 0])

        while queue:
            root, col = queue.popleft()
            res[col].append(root.val)
            if root.left:
                queue.append([root.left, col - 1])
            if root.right:
                queue.append([root.right, col + 1])
        min_i, max_i = min(res.keys()) , max(res.keys())       
        f = []
        for i in range(min_i, max_i + 1):
            f.append(res[i])
        return f