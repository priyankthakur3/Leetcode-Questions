class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board) , len(board[0])
        queue = collections.deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs_helper():

            while queue:
                r, c  = queue.popleft()
                board[r][c] = "U"
                for dx, dy in directions:
                    tx, ty = r + dx , c + dy
                    if 0 <= tx < ROWS and 0 <= ty < COLS and board[tx][ty] == "O":
                        queue.append((tx,ty))
            return
        
        for r in range(ROWS):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][COLS - 1] == "O":
                queue.append((r, COLS - 1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[ROWS - 1][c] == "O":
                queue.append((ROWS - 1, c))
        bfs_helper()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "U":
                    board[r][c] = "O"
        
        return