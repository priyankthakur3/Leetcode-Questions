class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0

        left = [0] * len(height)
        right = [0] * len(height)
        maxTemp = 0
        for i in range(len(height)):
            maxTemp = max(height[i],maxTemp)
            left[i] = maxTemp
        maxTemp = 0
        for i in range(len(height) - 1, -1,-1):
            maxTemp = max(height[i],maxTemp)
            right[i] = maxTemp
        res = 0
        for i in range(len(height)):
            res += min(left[i] , right[i]) - height[i]
        return res