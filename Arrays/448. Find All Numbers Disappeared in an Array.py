# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         counter = 1
#         tempArray = []
#         for i in range(len(nums)):
#             if nums[i] == counter:
#                 if i < len(nums) - 1 and nums[i + 1] == counter:
#                     continue
#             else:
#                 tempArray.append(counter)
#             counter +=1

#         return tempArray


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingVal = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
               nums[index] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missingVal.append(i + 1)

        return missingVal
