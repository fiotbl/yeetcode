class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palins = []
        
        def dfs(i):
            if i >= len(s):
                res.append(palins.copy())
                return
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    palins.append(s[i:j+1])
                    dfs(j+1)
                    palins.pop()
        dfs(0)
        return res
    
    def isPalin(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True
                