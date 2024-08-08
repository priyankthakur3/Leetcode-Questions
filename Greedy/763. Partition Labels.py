class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_pos = {}
        # hashmap to store last position of char
        for i, v in enumerate(s):
            end_pos[v] = i
        res = []
        end = size = 0
        for i in range(len(s)):
            size += 1
            end = max(end, end_pos[s[i]])
            # if i == end i.e. grouped all repeating chars together add size to res
            if i == end:
                res.append(size)
                size = 0
        return res
            