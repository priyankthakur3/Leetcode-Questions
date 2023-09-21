class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:

            temp = "".join(sorted(s))
            if temp not in hashmap:
                hashmap[temp] = []
            hashmap[temp].append(s)

        return hashmap.values()
