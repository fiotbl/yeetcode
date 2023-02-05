class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                    left = mat[i][j-1] if j > 0 else float('inf')
                    up = mat[i-1][j] if i > 0 else float('inf')       
                    mat[i][j] = min(left, up) + 1
                    
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if mat[i][j] != 0:
                    right = mat[i][j+1] if j < cols-1 else float('inf')
                    down = mat[i+1][j] if i < rows-1 else float('inf')       
                    mat[i][j] = min(min(right, down)+1, mat[i][j])
                    
        return mat