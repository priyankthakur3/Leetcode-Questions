class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.helper(candidates, 0 , target, [])
        return self.result


    def helper(self, candidates, index, target, path):
        if target < 0 or index == len(candidates):
            return
        elif target == 0:
            self.result.append(path[:])       
        else:
            # in order to differentiate between [2,2,3] and [2,3,2] and [3,2,2] 
            # start below loop from 0
            for i in range(index,len(candidates)):
                # action
                path.append(candidates[i])
                # recurse
                self.helper(candidates, i, target - candidates[i], path)
                # backtrack
                path.pop()
    