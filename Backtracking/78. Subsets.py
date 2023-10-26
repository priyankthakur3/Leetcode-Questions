class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def dfs_helper(index, path):

            if index >= len(nums):
                result.append(path[:])
                return

            # choose
            path.append(nums[index])
            dfs_helper(index + 1, path)

            # not choose
            path.pop()
            dfs_helper(index + 1, path)

        dfs_helper(0, [])
        return result
