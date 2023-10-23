class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs_helper(x,y):
            # x, y out of range or x,y not process/water return
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1":
                return
            # mark as processed
            grid[x][y] = "2"
            # search neighbouring elements
            for dx , dy in direction:
                dfs_helper(x + dx, y + dy)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # start from first occurence of 1
                if grid[row][col] == "1":
                    count += 1
                    dfs_helper(row,col)
        return count