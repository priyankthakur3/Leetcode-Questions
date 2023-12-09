class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        result = 0
        for n in uniq:
            if (n - 1) not in uniq:
                l_range = 1
                while n + 1 in uniq:
                    l_range += 1
                    n = n + 1
                result = max(result, l_range)
                if result > len(nums)//2:
                    break
        return result