class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, a in enumerate(heights):
            start = i
            while stack and stack[-1][1] > a:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, a])
        for i, a in stack:
            maxArea = max(maxArea, a * (len(heights) - i))    
        return maxArea