# Brute Force
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         min = 2^31 -1
#         for i in range(0,len(nums)):
#             if(nums[i]<min):
#                 min = nums[i]
#         return min


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        if nums[low] < nums[high]:
            return nums[low]

        while(low <= high):
            mid = low + (high -low)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[low] <= nums[mid]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid -1
        
        return -1



# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if(len(nums)==1):
#             return 0
        
#         # if(len(nums)==2):
#         #     return 1 if nums[0] < nums[1] else 0
        
#         low = 0
#         high = len(nums) -1

#         while (low <= high):
#             mid = low + (high-low)//2
#             if ( mid == 0 or nums[mid] > nums[mid - 1] ) and ( mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
#                 return mid
#             elif( mid > 0 and nums[mid-1] > nums[mid] ):
#                 high = mid-1
#             else:
#                 low = mid+1
#         return -1
        