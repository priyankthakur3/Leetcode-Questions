from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set) # key is r//3 and c//3

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if  (board[r][c] in rows[r] or # row check
                        board[r][c] in cols[c] or #col check
                        board[r][c] in square[(r//3 , c//3)]): #square check 
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
            
        return True