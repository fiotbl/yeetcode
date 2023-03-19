class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, path, total):
            if total > target or i >= len(candidates): return
            if total == target: 
                res.append(path.copy())
                return
            
            path.append(candidates[i])
            dfs(i, path, total+candidates[i])
            path.pop()
            dfs(i+1, path, total)
            
        dfs(0,[],0)
        return res
            