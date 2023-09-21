class Solution:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0],
                  [1, 1], [1, -1], [-1, 1], [-1, -1]]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        if not board or len(board) == 0:
            return

        # 0 --> 1  =  2
        # 1 --> 0  =  3

        for i in range(m):
            for j in range(n):
                count_alive = self.countAlive(board, i, j, m, n)

                # make dead
                if board[i][j] == 1 and (count_alive < 2 or count_alive > 3):
                    board[i][j] = 3

                # make alive
                if board[i][j] == 0 and count_alive == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0

        return

    def countAlive(self, board, i, j, m, n):
        result = 0
        for d in self.directions:
            nr = i + d[0]
            nc = j + d[1]
            if nr >= 0 and nc >= 0 and nr < m and nc < n and (board[nr][nc] == 1 or board[nr][nc] == 3):
                result += 1

        return result
