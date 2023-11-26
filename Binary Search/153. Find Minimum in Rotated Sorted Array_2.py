class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low , high = 0 , len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[low] < nums[high]:
                return nums[low]
            if (mid == 0 or nums[mid - 1] > nums[mid]) and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return -1