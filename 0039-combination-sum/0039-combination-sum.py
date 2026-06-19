class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i,path):
            if sum(path) == target:
                res.append(path[:])
                return
            
            if sum(path) > target:
                return
            
            for j in range(i,len(candidates)):
                path.append(candidates[j])
                backtrack(j,path)
                path.pop()
        backtrack(0,[])
        return res
