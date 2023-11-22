class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            # check if current temperature is greater than stack's top temp
            while stack and t > stack[-1][1]:
                # pop top element
                index, temp = stack.pop()
                res[index] = i - index
            stack.append([i, t])
        return res