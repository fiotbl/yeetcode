class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(L, R):
            if L == R == n:
                res.append(''.join(stack))
                return
            
            if L < n:
                stack.append("(")
                backtrack(L+1 , R)
                stack.pop()
                
            if R < L:
                stack.append(")")
                backtrack(L , R+1)
                stack.pop()
                
        backtrack(0, 0)
        return res