# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# TC: O(N)
# SC: O(N)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # stack to maintain flatten values
        self.stack = []
        # helper to get all values
        self.__dfs_helper(nestedList)
        # reverse stack to keep next operation O(1)
        self.stack.reverse()
    
    def __dfs_helper(self,nested):
        for n in nested:
            # if element in nested is Integer append
            # else run dfs
            if n.isInteger():
                self.stack.append(n.getInteger())
            else:
                self.__dfs_helper(n.getList())
    
    def next(self) -> int:
        return self.stack.pop()
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())