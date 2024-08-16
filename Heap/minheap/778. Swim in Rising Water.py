from heapq import heapify, heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [[grid[0][0], 0, 0]]
        visited, n = set(), len(grid) - 1
        while minHeap:
            t, tx, ty = heappop(minHeap)
            if tx == n and ty == n:
                return t
            for dx, dy in directions:
                r, c = dx + tx, dy + ty
                if 0 <= r <= n and 0 <= c <= n and (r, c) not in visited:
                    visited.add((r,c))
                    heappush(minHeap, [max(grid[r][c],t), r,c])
        return float('-inf')
        
