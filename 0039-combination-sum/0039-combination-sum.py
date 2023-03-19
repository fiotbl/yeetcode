class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[0] * (target+1) for _ in range(len(candidates)+1)]
        for i in range(len(candidates)+1):
            dp[i][0] = 1
        for i in range(1, len(candidates)+1):
            for j in range(1, target+1):
                if j < candidates[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-candidates[i-1]] + dp[i-1][j]
        res = []
        def backtrack(path, target, i):
            if target == 0:
                res.append(path)
            elif target > 0:
                for j in range(i, len(candidates)):
                    backtrack(path + [candidates[j]], target - candidates[j], j)
        backtrack([], target, 0)
        return res