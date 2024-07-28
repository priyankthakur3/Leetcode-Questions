class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [-1 for _ in range(len(cost))]

        def helper(n):

            if n < 0 or n >= len(cost):
                return 0

            if n <= 1:
                return cost[n]

            if dp[n] != -1:
                return dp[n]
            
            dp[n] = cost[n] + min( helper(n - 1), helper(n - 2))
            return dp[n]
        
        return min(helper(len(cost) -1), helper(len(cost) - 2))