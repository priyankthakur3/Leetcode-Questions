class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minCost = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - minCost)
            minCost = min(minCost, prices[i])
        return profit