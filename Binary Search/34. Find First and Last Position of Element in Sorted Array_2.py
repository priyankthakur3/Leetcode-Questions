class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(left, leftBias):
            right = len(nums) - 1
            i = -1
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    i = mid
                    if not leftBias:
                        left = mid + 1
                    else:
                        right = mid - 1
            return i

        left = binarySearch(0, True)
        if left == -1:
            return [-1, -1]
        right = binarySearch(left, False)
        return [left, right]
            