class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2, 3:3}
        
        def dfs(n):
            if n in memo: return memo[n]
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]
        
        return dfs(n)