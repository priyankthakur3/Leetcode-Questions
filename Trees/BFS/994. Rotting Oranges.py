from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        orange_count = 0
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    orange_count += 1
            # append all rotten oranges to queue
                elif grid[row][col] == 2:
                    queue.append((row, col))

        minutes = 0

        while queue and orange_count != 0:
            minutes += 1
            # process oranges level by level
            # increase minute only if all adjacent elements are processed
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for tx, ty in directions:
                    dx, dy = x + tx, y + ty
                    # check if adjacent elements are not rotten, make them rotten and add it to queue
                    if dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]):
                        if grid[dx][dy] == 1:
                            grid[dx][dy] = 2
                            orange_count -= 1
                            queue.append((dx, dy))

        return minutes if orange_count == 0 else -1
