class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(idx, path, target):

            if target == 0:
                res.append(path[:])
                return
            
            if target < 0 or idx == len(candidates):
                return
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                helper(i + 1, path, target - candidates[i])
                path.pop()
                prev = candidates[i]
        
        helper(0, [], target)
        return res