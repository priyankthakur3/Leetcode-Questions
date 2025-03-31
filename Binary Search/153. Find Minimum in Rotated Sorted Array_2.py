class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0 , len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2
            # best case
            if nums[low] < nums[high]:
                return nums[low]

            # check if mid element is pivot element
            elif (mid == 0 or nums[mid] < nums[mid -1]) and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            # check if left portion is sorted
            elif nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid -1
        
        return -1
            