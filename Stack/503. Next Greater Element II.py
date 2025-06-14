class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [ -1] * len(nums)

        for i in range(2 * len(nums) - 1, -1 ,-1):
            
            current_num = nums[i % len(nums)]
            while stack and current_num >= stack[-1]:
                stack.pop()
            
            if i < len(nums):
                if stack:
                    res[i] = stack[-1]
            stack.append(current_num)
        return res
