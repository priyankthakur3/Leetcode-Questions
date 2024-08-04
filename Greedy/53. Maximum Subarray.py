class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = currSum = float('-inf')
        for i in range(len(nums)):
            
            if currSum < 0:
                currSum = 0
            currSum += nums[i]

            maxVal = max(maxVal, currSum)
        return maxVal
