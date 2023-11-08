class Solution:
    def tribonacci(self, n: int) -> int:
        dict = {0:0, 1:1, 2:1}
        
        def memo(n):
            if n in dict: return dict[n]
            dict[n] = memo(n-1) + memo(n-2) + memo(n-3)
            return dict[n]
        
        return memo(n)