class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(num):
            
            if len(num) == 1:
                return num[0]
            dp = [ 0 for _ in range(len(num))]

            dp[0] = num[0]
            dp[1] = max(num[1], num[0])
            for i in range(2, len(num)):
                dp[i]  = max(dp[i - 2] + num[i], dp[i - 1])
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))