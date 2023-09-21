class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        n = len(nums)-1
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if(sum == k):
                    counter += 1
        return counter
