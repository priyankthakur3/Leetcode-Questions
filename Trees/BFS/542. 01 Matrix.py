from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                # add all zero to queue
                # mark 1's as -1 unvisited
                if mat[row][col] == 0:
                    queue.append([row, col])
                else:
                    mat[row][col] = -1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                tx, ty = queue.popleft()
                for dx, dy in directions:
                    x, y = tx + dx, ty + dy
                    # check if neighbouring x and y are within range and its initial value is -1
                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == -1:
                        # get distance of row, col due to which its added to queue and increment
                        mat[x][y] = mat[tx][ty] + 1
                        queue.append([x, y])
        return mat
