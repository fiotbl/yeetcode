class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(countL, countR, curr):
            if countR == n and countL == n:
                res.append(curr)
                return
            if countL < n:
                curr += "("
                dfs(countL + 1, countR, curr)
                curr = curr[:-1]
            if countR < countL:
                curr += ")"
                dfs(countL, countR+1, curr)
                curr = curr[:-1]

        
        dfs(0,0,"")
        return res