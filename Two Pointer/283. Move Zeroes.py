class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for r in range(len(nums)):
            if nums[r] and nums[s] == 0:
                nums[r], nums[s] = nums[s],nums[r]
            if nums[s] != 0:
                s += 1