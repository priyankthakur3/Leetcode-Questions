from heapq import heapify, heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hashmap = {}
        for n in hand:
            hashmap[n] = 1 + hashmap.get(n , 0)
        
        minHeap = list(hashmap.keys())
        heapify(minHeap)

        while minHeap:
            top = minHeap[0]
            for i in range(top, top + groupSize):
                # base condition
                if i not in hashmap:
                    return False
                hashmap[i] -= 1

                # if all cards are processed i.e. count == 0
                if hashmap[i] == 0:
                    # check if i is still at top of hashmap
                    if i != minHeap[0]:
                        return False
                    heappop(minHeap)
            
        return True