from collections import defaultdict
from heapq import heappush, heappop
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.sentence = ''
        for i in range(len(sentences)):
            self.add(sentences[i], times[i])
        

    def add(self, s, cnt):
        curr = self.root
        for ch in s:
            curr = curr.children[ch]
            # maintain count of each word's occurence 
            curr.cnt[s] += cnt
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add(self.sentence, 1)
            self.curr= self.root
            self.sentence = ''
            return []
        else:
            self.sentence += c
            self.curr = self.curr.children[c]
            results =[]
            records_heap = []
            # to get top 3 records
            for st, cnt in self.curr.cnt.items():
                heappush(records_heap, (-cnt, st))
            for i in range(3):
                if records_heap and len(records_heap) > 0:
                    c,s = heappop(records_heap)
                    results.append(s)
            return results


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)