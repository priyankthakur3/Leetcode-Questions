class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(maze), len(maze[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        
        def helper(r,c):
            if visited[r][c]:
                return False
            
            if r == destination[0] and c == destination[1]:
                return True
            visited[r][c] = True
            for dx, dy in directions:
                tx, ty = r , c 
                while 0 <= tx < ROWS and 0 <= ty < COLS and maze[tx][ty] == 0:
                    tx += dx
                    ty += dy
                tx -= dx
                ty -= dy
                if helper(tx, ty):
                    return True
            return False
        
        return helper(start[0],start[1])
