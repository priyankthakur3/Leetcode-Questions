class TrieNode:

    def __init__(self):
        self.char = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            char_ascii = ord(char) - ord('a')
            if not curr.char[char_ascii]:
                curr.char[char_ascii] = TrieNode()
            curr = curr.char[char_ascii]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            char_ascii = ord(char) - ord('a')
            if not curr.char[char_ascii]:
                return False
            curr = curr.char[char_ascii]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            char_ascii = ord(char) - ord('a')
            if not curr.char[char_ascii]:
                return False
            curr = curr.char[char_ascii]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
