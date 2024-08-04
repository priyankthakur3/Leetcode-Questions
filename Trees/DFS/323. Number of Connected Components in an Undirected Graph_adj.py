class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_mat = { i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_mat[n1].append(n2)
            adj_mat[n2].append(n1)
           
        connected, visited = 0, set()

        def helper(i):
            if i in visited:
                return False
            visited.add(i)
            for nxt in adj_mat[i]:
                helper(nxt)
            return True
        
        for i in range(n):
            if helper(i):
                connected += 1
        
        return connected
