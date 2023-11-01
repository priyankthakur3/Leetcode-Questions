class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def longestWord(self, words):
        root = TrieNode()
        self.longest = ""
        for word in sorted(words):
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_end = True

        def dfs(root, local_word):
            if not root.is_end:
                return

            if len(local_word) > len(self.longest):
                self.longest = local_word

            for ch, node in root.children.items():
                if node.is_end:
                    dfs(node, local_word + ch)

        for ch in root.children:
            dfs(root.children[ch], ch)

        return self.longest
