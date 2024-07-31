from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(rooms) , len(rooms[0])
        INF = 2 ^ 31 - 1
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        distance = 0
        while queue:
            lvl = len(queue)
            distance += 1
            for _ in range(lvl):
                r, c = queue.popleft()
                for dx, dy in directions:
                    tr , tc = r + dx, c + dy
                    if 0 <= tr < ROWS and 0 <= tc < COLS and rooms[tr][tc] == 2147483647:
                        rooms[tr][tc] = distance
                        queue.append((tr,tc))
