from heapq import heapify, heappush, heappop
class MedianFinder:

    def __init__(self):
        # small is max heap, large is min heap
        self.small, self.large = [],[]
        heapify(self.small)
        heapify(self.large)

    def addNum(self, num: int) -> None:
        
        if self.large and self.large[0] < num:
            heappush(self.large, num)
        else:    
            heappush(self.small, -1 * num)
        # check if heaps is of uneven length
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -1 * heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heappush(self.small, -1 * heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ( -1 * self.small[0] + self.large[0] ) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()