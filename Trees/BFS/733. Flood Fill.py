from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        color_prev = image[sr][sc]

        if color_prev == color:
            return image

        queue = deque([(sr, sc)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            image[x][y] = color

            for dx, dy in directions:
                tx, ty = x + dx, y + dy
                if 0 <= tx < rows and 0 <= ty < cols and image[tx][ty] == color_prev:
                    queue.append((tx, ty))

        return image
