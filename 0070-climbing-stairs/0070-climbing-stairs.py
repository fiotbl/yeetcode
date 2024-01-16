class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2, 3:3}
        
        def steps(n):
            if n in memo: return memo[n]
            
            memo[n] = steps(n-1) + steps(n-2)
            return memo[n]
        
        return steps(n)