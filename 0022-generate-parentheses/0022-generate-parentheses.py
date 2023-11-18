class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(numL, numR):
            if numL == numR == n:
                res.append("".join(stack))
                return
            
            if numL < n:
                stack.append("(")
                backtrack(numL + 1, numR)
                stack.pop()
            
            if numR < numL:
                stack.append(")")
                backtrack(numL, numR + 1)
                stack.pop()
            
        backtrack(0,0)
        return res