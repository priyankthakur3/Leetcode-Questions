class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = collections.deque()
        count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs():
            while queue:
                tx, ty = queue.popleft()
                for dx, dy in directions:
                    x, y = tx + dx, ty + dy
                    # iterate through neighbouring nodes and check if they are land and not water
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                        grid[x][y] = "2"
                        queue.append([x, y])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    # if island is detect increment counter and run bfs until boundaries
                    count += 1
                    queue.append([row, col])
                    bfs()
                    grid[row][col] = "2"

        return count
