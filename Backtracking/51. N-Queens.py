class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []

        board = [[False for _ in range(n)] for _ in range(n)]
        self.dfs(board, 0, n)

        return self.result

    def dfs(self, board, r, n):
        if r == n:
            self.result.append(
                ["".join(["Q" if i else "." for i in row]) for row in board])

        for j in range(n):
            if self.isSafe(board, r, j, n):
                # action
                board[r][j] = True
                # recurse
                self.dfs(board, r + 1, n)
                # backtrack
                board[r][j] = False

    def isSafe(self, board, r, c, n):
        for i in range(r):
            if board[i][c]:
                return False

        # uppper left
        i, j = r, c
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        # upper right
        i, j = r, c
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1
        return True
