# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        # initialize result and append to queue
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            # loop through all nodes for level
            for _ in range(len(queue)):
                temp = queue.popleft()
                # important to put left then right child
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # add last element which was popped out from queue
            result.append(temp.val)
    
        return result
        