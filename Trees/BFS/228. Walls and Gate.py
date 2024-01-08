from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS , COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                visited.add((r,c))
                for tx, ty in directions:
                    x, y = r + tx, c + ty
                    if (0 <= x < ROWS 
                        and 0 <= y < COLS 
                        and (x,y) not in visited 
                        and grid[x][y] == 2147483647) :
                        grid[x][y] = grid[r][c] + 1
                        queue.append((x,y))