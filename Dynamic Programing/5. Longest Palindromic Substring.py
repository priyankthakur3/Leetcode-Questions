class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, res = len(s), ''
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if len(s[l : r + 1]) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1

            l, r = i, i 
            while l >= 0 and r < n and s[l] == s[r]:
                if len(s[l : r + 1]) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res
        