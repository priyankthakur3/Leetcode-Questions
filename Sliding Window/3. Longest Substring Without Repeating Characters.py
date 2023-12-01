class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni_char = set()
        left = ans = 0
        for i in range(len(s)):
            while s[i] in uni_char:
                uni_char.remove(s[left])
                left += 1
            uni_char.add(s[i])
            ans = max(ans, i - left + 1)
        return ans