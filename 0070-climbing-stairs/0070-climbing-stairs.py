class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        
        def stairs(n):
            if n in memo: return memo[n]
            
            memo[n] = stairs(n-1) + stairs(n-2)
            
            return memo[n]
        
        return stairs(n)