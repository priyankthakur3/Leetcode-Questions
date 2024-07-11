class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1

        col_set = set()
        p_set = set()
        n_set = set()
        board = [['.'] * n for _ in range(n)]
        self.output = 0

        def helper(r , board):

            if r == n:
                self.output += 1
                return
            for c in range(n):
                if c in col_set or (r + c) in p_set or (r - c) in n_set:
                    continue

                board[r][c] = 'Q'
                col_set.add(c)
                p_set.add(r + c)
                n_set.add(r - c)

                helper(r + 1, board)

                board[r][c] = '.'
                col_set.remove(c)
                p_set.remove(r + c)
                n_set.remove(r - c)
            
        helper(0, board)
        return self.output