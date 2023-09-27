## brute force
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(0,len(nums)):
#             for j in range(0, len(nums)-i-1):
#                 if nums[j] > nums[j+1]:
#                     temp = nums[j+1]
#                     nums[j+1] = nums[j]
#                     nums[j] = temp


class Solution:
    def swapNums(self, nums: List[int], p1: int, p2: int):
        temp = nums[p2]
        nums[p2] = nums[p1]
        nums[p1] = temp

    def sortColors(self, nums: List[int]) -> None:
        left, pivot, right = 0, 0, len(nums)-1
        while pivot <= right:
            if nums[pivot] == 0:
                self.swapNums(nums, pivot, left)
                pivot += 1
                left += 1
            elif nums[pivot] == 2:
                self.swapNums(nums, pivot, right)
                right -= 1
            else:
                pivot += 1
