class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res
