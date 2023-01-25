class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        col = set()
        negSlope = set() # (r+c)
        posSlope = set() # (r-c)
        res = []

        
        def backtracking(r):
            if r == n:
                ans = ["".join(n) for n in board]
                res.append(ans)
                return 
            
            for c in range(n):
                if c in col or (r-c) in posSlope or (r+c) in negSlope:
                    continue
                else:
                    board[c][r] = "Q"
                    negSlope.add(r+c)
                    posSlope.add(r-c)
                    col.add(c)
                    
                    backtracking(r+1)
                    
                    board[c][r] = "."
                    negSlope.remove(r+c)
                    posSlope.remove(r-c)
                    col.remove(c)
                    
        backtracking(0)
        return res
                    
                
            
        
        