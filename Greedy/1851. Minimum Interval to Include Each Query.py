class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res, i  = {}, 0
        minHeap = []

        for q in sorted(queries):
            
            # add all intervals which are less than or equal to query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # pop all intervals which are less than current query
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # assign minlength to that query
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]