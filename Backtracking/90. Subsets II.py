class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def helper(idx, subset):

            if idx == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[idx])
            helper(idx + 1, subset)
            subset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            helper(idx + 1, subset)            

        helper(0,[])
        return result