class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        queue = deque([start])
        while queue:
            # pop last position of ball
            r, c = queue.popleft()
            if r == destination[0] and c == destination[1]:
                return True
            visited.add((r,c))
            for tr, tc in directions:
                dx, dy = r , c 
                # roll the ball around untill it hits wall
                while 0 <= (dx + tr) < ROWS and 0 <= (dy + tc) < COLS and maze[dx + tr][dy + tc] == 0:
                    dx += tr
                    dy += tc
                # add position where it has hit wall
                if (dx, dy) in visited:
                    continue
                queue.append([dx,dy])
        return False
