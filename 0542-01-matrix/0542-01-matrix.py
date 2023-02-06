class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]!=0:
                    up = mat[i-1][j] if i>0 else float('inf')
                    left = mat[i][j-1] if j>0 else float('inf')         
                    mat[i][j] = min(up, left) + 1
                    
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j]!=0:
                    down = mat[i+1][j] if i<len(mat)-1 else float('inf')
                    right = mat[i][j+1] if j<len(mat[0])-1 else float('inf')         
                    mat[i][j] = min(mat[i][j], min(down, right) + 1)
        
        return mat