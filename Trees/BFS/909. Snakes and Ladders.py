class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def getRowCol(square):
            row , col = (square - 1) // n, (square - 1) % n
            # if odd rows flip cols
            if row % 2:
                col = n - 1 - col
            return row, col
        
        
        q = deque() # [square, steps]
        q.append([1, 0])
        visited = set()
        while q:
            sq, steps = q.popleft()
            for i in range(1, 7):
                nxt = sq + i
                r, c = getRowCol(nxt)
                # in case of ladder/snake go to next position
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt == n * n:
                    return steps + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, steps + 1])
        return -1
