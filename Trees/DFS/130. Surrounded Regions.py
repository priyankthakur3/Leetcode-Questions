class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0], [0,1],[0,-1]]

        def dfs_helper(r, c):
            """
            DFS function for capturing unbounded region
            """
            if board[r][c] != "O":
                return
            # mark as unbounded
            board[r][c] = "U"
            for dx, dy in directions:
                tx, ty = r + dx, c + dy
                if 0 <= tx < ROWS and 0 <= ty < COLS:
                    dfs_helper(tx, ty)
        
        # STEP 1: capture all unbounded region
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and ( r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs_helper(r,c)

        # STEP 2: Convert all bound "O" to "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # STEP 3: Convert all unbounded "O" (U) to O

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "U":
                    board[r][c] = "O"
        
        return