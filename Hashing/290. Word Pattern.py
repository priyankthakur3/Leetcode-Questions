class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        patternMap = {}
        sMap = set()
        sArr = s.split()

        if len(sArr) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in patternMap:
                if patternMap[pattern[i]] != sArr[i]:
                    return False

            else:
                if sArr[i] in sMap:
                    return False
                else:
                    patternMap[pattern[i]] = sArr[i]
                    sMap.add(sArr[i])
        return True
