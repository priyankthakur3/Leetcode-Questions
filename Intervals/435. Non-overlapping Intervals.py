class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start,end in intervals[1:]:
            # check if interval falls between prev interval
            # if not move to next interval
            if start >= prevEnd:
                prevEnd = end
            else:
                # if yes then choose interval with lowest range
                res+= 1
                prevEnd = min(prevEnd, end)

        return res