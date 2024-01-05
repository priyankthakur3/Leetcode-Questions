class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        result = []
        ROWS, COLS = len(heights), len(heights[0])
        def dfs_helper(r, c, visited, prev_height):

            if (r,c) in visited or heights[r][c] < prev_height:
                return
            visited.add((r,c))

            for dx, dy in directions:
                tx, ty = r + dx, c + dy
                if 0 <= tx < ROWS and 0 <= ty < COLS:
                    dfs_helper(tx, ty, visited, heights[r][c])
            
        atl , pac = set() , set()
        for r in range(ROWS):
            dfs_helper(r, 0, pac, heights[r][0])
            dfs_helper(r, COLS - 1, atl, heights[r][COLS - 1])

        for c in range(COLS):
            dfs_helper(0, c, pac, heights[0][c])
            dfs_helper(ROWS - 1, c , atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r, c) in pac:
                    result.append([r,c])
        
        return result
