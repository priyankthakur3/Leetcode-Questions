class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    
    def get_prefix(self, word):
        prefix = ""
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return word
            prefix += ch
            curr = curr.children[ch]
            if curr.is_end:
                break
            
        return prefix
             

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # build Trie tree
        T = Trie()
        for word in dictionary:
            T.insert(word)
        # split string and replace with corresponding prefix
        split_string = sentence.split(" ")
        return " ".join([T.get_prefix(word) for word in split_string])
        