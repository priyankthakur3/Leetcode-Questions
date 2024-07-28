# bottom up approach
class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helper(n, dp):
            
            # base condition
            if n <= 1:
                return 1
            
            if n in dp:
                return dp[n]
            
            dp[n] = helper(n - 1, dp) + helper(n -2 , dp)
            return dp[n]
        return helper(n, {}) 