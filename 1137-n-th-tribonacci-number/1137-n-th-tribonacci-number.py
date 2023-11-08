class Solution:
    def tribonacci(self, n: int) -> int:
        dict = {}
        
        def memo(n):
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1
            if n in dict: return dict[n]
            else: dict[n] = memo(n-1) + memo(n-2) + memo(n-3)
            return dict[n]
        
        return memo(n)