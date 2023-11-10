class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {1:1, 2:2, 3:3}
        
        def memo(n):
            if n in dic: return dic[n]
            dic[n] = memo(n-1) + memo(n-2)
            return dic[n]
        
        return memo(n)