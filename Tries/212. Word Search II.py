class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class TrieNode:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = Node()
            curr = curr.children[s]
        curr.is_end = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for s in words:
            trie.add(s)
        
        res = []
        R , C = len(board), len(board[0])
        
        def dfs_helper(r, c, root, word):

            if (board[r][c] == "#" or board[r][c] not in root.children ):
                return

            # action
            root = root.children[board[r][c]]
            word += board[r][c]
            tmp = board[r][c]
            board[r][c] = "#"
            
            
            if root.is_end:
                res.append(word)
                root.is_end = False
            
            # recurse
            for dx, dy in directions:
                tx, ty = r + dx, c + dy
                if 0 <= tx < R and 0 <= ty < C:
                    dfs_helper(tx, ty, root, word)
            # backtrack
            board[r][c] = tmp
        
        
        for r in range(R):
            for c in range(C):
                dfs_helper(r, c, trie.root, "")
        return res
