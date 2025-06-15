class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0
        # check if boundary doesnot exceeds len(nums)
        while r < len(nums) -1:
            farthest = 0
            for i in range(l, r + 1):
                # calculate farthest jump possible using values in our current window
                farthest = max(farthest, i + nums[i])
            # move window
            l = r + 1
            r = farthest
            res += 1
        return res
