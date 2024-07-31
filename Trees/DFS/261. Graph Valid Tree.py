class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        d_map = {i: set() for i in range(n)}

        for n1, n2 in edges:

            d_map[n1].add(n2)
            d_map[n2].add(n1)
        visited = set()
        
        def dfs_helper(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for dep in d_map[node]:
                if dep == prev:
                    continue
                if not dfs_helper(dep, node):
                    return False
            return True
        
        return dfs_helper(0, -1) and len(visited) == n