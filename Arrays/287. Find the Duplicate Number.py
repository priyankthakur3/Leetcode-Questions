class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return idx
            nums[idx] = -1 * abs(nums[idx])
        return 0