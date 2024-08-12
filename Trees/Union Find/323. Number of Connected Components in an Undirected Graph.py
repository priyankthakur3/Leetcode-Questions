class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]


        def find(n1):
            while n1 != par[n1]:
                n1 = par[n1]
            return n1
        
        def union(n1, n2):
            
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = par[p1]
                rank[p1] += 1
            return 1

        res = n
        for a, b in edges:
            res -= union(a, b)
        return res
