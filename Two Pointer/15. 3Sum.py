class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, a in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                val_sum = a + nums[left] + nums[right]
                if val_sum < 0:
                    left += 1
                elif val_sum > 0:
                    right -= 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
