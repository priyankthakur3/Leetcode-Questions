class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = self.sortWords(s)
        sortedT = self.sortWords(t)
        return len(s) == len(t) and sortedS == sortedT

    def sortWords(self, s: str) -> str:
        freq = 1
        for c in s:
            freq *= (ord(c) - ord('a') + 1)
        return freq
