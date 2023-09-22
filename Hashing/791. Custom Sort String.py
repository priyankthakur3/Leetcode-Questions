from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_map = defaultdict(lambda: 0)  # assign default value of 0 to all
        result = ""
        for ch in s:
            freq_map[ch] += 1

        for ch in order:
            result += ch*freq_map[ch]
            del freq_map[ch]

        for ch in freq_map.keys():
            result += ch*freq_map[ch]

        return result
