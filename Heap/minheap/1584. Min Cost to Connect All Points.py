from heapq import heapify, heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj_mat = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range( i + 1, len(points)):
                # calculate manhattan distance
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # add distance to both points as edge is bidirectional
                adj_mat[i].append([dist, j]) # [cost, index]
                adj_mat[j].append([dist, i]) # [cost, index]

        minHeap = []
        heappush(minHeap, [0,0])
        res = 0
        visited = set()
        while len(visited) < len(points):
            cost, idx = heappop(minHeap)
            if idx in visited:
                continue
            visited.add(idx)
            res += cost
            for cost, idx in adj_mat[idx]:
                if idx not in visited:
                    heappush(minHeap, [cost, idx])
        return res

