class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        time.sort(key=lambda x: (x[0], x[1]))
        max_count = 0
        r_sum = 0
        for t in time:
            r_sum += t[1]
            max_count = max(max_count,r_sum)
        return max_count