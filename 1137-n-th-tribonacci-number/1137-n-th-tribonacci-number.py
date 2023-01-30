class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        
        def recursion(n):
            if n in memo: return memo[n]
            memo[n] = recursion(n-3) + recursion(n-2) + recursion(n-1)
            return memo[n]
        
        return recursion(n)