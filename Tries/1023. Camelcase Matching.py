class Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
    def find(self, word,pattern):
        curr = self.root
        i = 0
        n = len(pattern)
        for c in word:
            if c.isupper():
                if i == n or c != pattern[i]:
                    return False
                i += 1
            elif c.islower() :
                if i < n and c == pattern[i]:
                    i+= 1
            curr = curr.children[c]
                            
        return i == len(pattern)
        

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        t = Trie()
        for word in queries:
            t.insert(word)
        res = []
        for word in queries:
            res.append(t.find(word,pattern))
        return res