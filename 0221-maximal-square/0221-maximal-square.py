class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix[0])
        cols = len(matrix)
        maxSide = 0
        
        dp = [[0]*(rows+1) for _ in range(cols+1)]
        
        for c in range(cols):
            for r in range(rows):
                if matrix[c][r] == "1":
                    dp[c+1][r+1] = min(dp[c+1][r], dp[c][r], dp[c][r+1]) + 1
                maxSide = max(maxSide, dp[c+1][r+1])
        print(dp)
        return maxSide * maxSide