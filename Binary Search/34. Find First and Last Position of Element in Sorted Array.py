# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         low = 0
#         high = len(nums) - 1

#         while low <= high:
#             mid = low + (high - low) // 2

#             if nums[mid] == target:
#                 start = mid
#                 end = mid

#                 # Find the start position of the target
#                 while start > 0 and nums[start - 1] == target:
#                     start -= 1

#                 # Find the end position of the target
#                 while end < len(nums) - 1 and nums[end + 1] == target:
#                     end += 1

#                 return [start, end]

#             elif nums[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1

#         return [-1, -1]

# brute force
# class Solution:


#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         def binarySearchLeft(nums: List[int],target: int) -> List[int]:
#             left = 0
#             right = len(nums)
#             while(left<=right):
#                 mid = left + (right-left)//2

#                 if(nums[mid]>=target):
#                     left = mid+1
#                 elif(nums[mid]>target):
#                     right = mid-1
#                 if(nums[mid]==target):
#                     return mid
#                 return -1

#         def binarySearchRight(nums: List[int],target: int) -> List[int]:
#             left = 0
#             right = len(nums)
#             while(left<=right):
#                 mid = left + (right-left)//2
#                 if(nums[mid]<=target):
#                     left = mid+1
#                 elif(nums[mid]>target):
#                     right = mid-1
#                 if(nums[mid]==target):
#                     return mid
#                 return -1
#         leftPos = binarySearchLeft(nums,target)
#         rightPos = binarySearchRight(nums,target)

#         return [leftPos,rightPos]
class Solution:
    def binarySearchFirst(self, low: int, high: int, target: int, nums: List[int]) -> int:
        while low <= high:
            mid = low + (high - low)//2
            if(nums[mid] == target):
                if(mid == 0 or nums[mid-1] < nums[mid]):
                    return mid
                else:
                    high = mid-1
            elif(nums[mid] > target):
                high = mid-1
            else:
                low = mid+1
        return -1

    def binarySearchSecond(self, low: int, high: int, target: int, nums: List[int]) -> int:
        while low <= high:
            mid = low + (high - low)//2
            if(nums[mid] == target):
                if(mid == len(nums) - 1 or nums[mid] < nums[mid+1]):
                    return mid
                else:
                    low = mid+1
            elif(nums[mid] > target):
                high = mid-1
            else:
                low = mid+1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if(len(nums) == 0 or nums is None):
            return [-1, -1]

        if(nums[0] > target or nums[-1] < target):
            return [-1, -1]

        lowestIndex = self.binarySearchFirst(0, len(nums), target, nums)
        if(lowestIndex == -1):
            return [-1, -1]
        highestIndex = self.binarySearchSecond(
            lowestIndex, len(nums), target, nums)

        return [lowestIndex, highestIndex]
