# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # method to all left childrens until end
    def __add_left(self, curr) -> None:
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # add all left elements to stack
        self.__add_left(root)

    def next(self) -> int:
        curr = self.stack.pop()
        # check if right element exists and add its corresponding left element to stack
        if curr.right:
            self.__add_left(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
