from collections import deque
from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        for task in tasks:
            if task not in task_count:
                task_count[task] = 0
            task_count[task] += 1
        q = deque()
        heap = [ -tcnt for task, tcnt in task_count.items()]
        heapify(heap)
        time = 0
        while heap or q:
            time += 1
            if heap:
                task = heappop(heap)
                cnt = 1 + task
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        
        return time