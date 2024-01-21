from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(heights), len(heights[0])

        def bfs_helper(queue,visited):
            while queue:
                r, c = queue.popleft()
                visited.add((r,c))
                for tx, ty in directions:
                    x, y = r + tx, c + ty
                    if 0 <= x < ROWS and 0 <= y < COLS and (x,y) not in visited and heights[x][y] >= heights[r][c]:
                        queue.append((x,y))
            return visited
        
        atl , pac = deque(), deque()

        for r in range(ROWS):
            atl.append((r, COLS - 1))
            pac.append((r, 0))
        
        for c in range(COLS):
            atl.append((ROWS - 1, c))
            pac.append((0, c))
        
        atl_set = bfs_helper(atl, set())
        pac_set = bfs_helper(pac, set())

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl_set and (r,c) in pac_set:
                    result.append([r,c])
        
        return result