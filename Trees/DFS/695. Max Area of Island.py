class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maxArea = 0

        def dfs_helper(r, c):

            if ( r < 0 or r >= len(grid)
            or c < 0 or c >= len(grid[0])
            or grid[r][c] != 1):
                return 0
            grid[r][c] = 2
            area = 1
            for dx, dy in directions:
                x , y = r + dx, c + dy
                area += dfs_helper(x, y)
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs_helper(i,j))
        
        return maxArea