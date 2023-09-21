class Solution:
    def longestPalindrome(self, s: str) -> int:
        setChar = set()
        count = 0
        for i in range(len(s)):
            if(s[i] in setChar):
                setChar.remove(s[i])
                count += 2
            else:
                setChar.add(s[i])

        if(len(setChar) > 0):
            count += 1

        return count
