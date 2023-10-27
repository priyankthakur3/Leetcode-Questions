class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def dfs_helper(index, partition):
            if index >= len(s):
                result.append(partition[:])
                return

            for i in range(index, len(s)):
                if __is_palindrome(s, index, i):
                    # action
                    partition.append(s[index: i + 1])
                    # recurse
                    dfs_helper(i + 1, partition)
                    # backtrack
                    partition.pop()

        def __is_palindrome(s, i, j):

            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        dfs_helper(0, [])
        return result
