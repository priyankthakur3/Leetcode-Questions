'''
E - > Empty
M - > mine
X - > revealed mine
'''
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        ROWS, COLS = len(board), len(board[0])
        
        def helper(r, c):
            pos = 0
            for tx, ty in directions:
                dx, dy = r + tx, c + ty
                if 0 <= dx < ROWS and 0 <= dy < COLS and board[dx][dy] == 'M':
                    pos += 1
            return pos

        x, y = click
        if board[x][y] == "M":
            board[x][y] = 'X'
        else:
            pos = helper(x,y)
            # if there is a mine in visinity
            if pos:
                board[x][y] = str(pos)
            else:
            # else keep iterating
                board[x][y] = 'B'
                for tx, ty in directions:
                    dx, dy = x + tx, y + ty
                    # check if within bounds and simulate clicks for all neighbouring cells
                    if 0 <= dx < ROWS and 0 <= dy < COLS and board[dx][dy] != "B":
                        self.updateBoard(board, [dx, dy])
        return board