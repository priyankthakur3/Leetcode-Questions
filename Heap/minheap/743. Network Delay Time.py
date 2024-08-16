from heapq import heapify, heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i : [] for i in range(n + 1) }

        for src, dest, w in times:
            adj[src].append([w, dest])
        minHeap = [[0, k]]
        heapify(minHeap)
        t, visited = 0, set()
        while minHeap:
            w1, nd = heappop(minHeap)
            if nd in visited:
                continue
            visited.add(nd)
            t = w1
            for w2, nd2 in adj[nd]:
                if nd2 not in visited:
                    heappush(minHeap, [w1 + w2, nd2])
        return t if len(visited) == n else -1