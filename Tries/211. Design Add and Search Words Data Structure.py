class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.maxLen = 0

    def addWord(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.is_end = True
        self.maxLen = max(self.maxLen, len(word))

    def search(self, word: str) -> bool:
        if len(word) > self.maxLen: return False
        def dfs_helper(root, idx):
            curr = root

            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs_helper(child, i + 1):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.is_end
        return dfs_helper(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)