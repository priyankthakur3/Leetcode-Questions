class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        n_diag = set()  # ( r - c ) up to down
        p_diag = set()  # ( r + c ) down to up
        result = []
        board = [['.'] * n for i in range(n)]

        def dfs_helper(row, board):

            if row >= n:
                board_copy = ["".join(r) for r in board]
                result.append(board_copy)
                return

            for col in range(n):
                if col in col_set or (row - col) in n_diag or (row + col) in p_diag:
                    continue
                # action
                col_set.add(col)
                n_diag.add(row - col)
                p_diag.add(row + col)
                board[row][col] = "Q"
                # recurse
                dfs_helper(row + 1, board)
                # backtrack
                col_set.remove(col)
                n_diag.remove(row - col)
                p_diag.remove(row + col)
                board[row][col] = "."

        dfs_helper(0, board)
        return result
