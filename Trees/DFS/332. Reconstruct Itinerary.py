from heapq import heappush, heapify, heappop
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)
        
        for src in adj.keys():
            heapify(adj[src])
        ans = []

        def dfs_helper(src):

            while adj[src]:
                des = heappop(adj[src])
                dfs_helper(des)
            
            ans.append(src)
        
        dfs_helper("JFK")

        return ans[::-1]