class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        boardDic = collections.defaultdict(int)

        for row in board:
            for elm in row:
                boardDic[elm] += 1
        # if all character doesnot exits in board return false
        for ch in word:
            if boardDic[ch] < 1:
                return False

        def dfs(r, c, charIdx):
            # base condition if charIdx is out of range or word is not equal
            if word[charIdx] != board[r][c] or charIdx >= len(word):
                return False
            # if charIdx is equal to len of word
            if charIdx == len(word) - 1:
                return True

            # traverse
            for x, y in directions:
                # action
                tmp = board[r][c]
                board[r][c] = "#"
                tx, ty = r + x, c + y
                if 0 <= tx < len(board) and 0 <= ty < len(board[0]):
                    # recurse
                    if dfs(tx, ty, charIdx + 1):
                        return True
                # backtrack
                board[r][c] = tmp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False
