class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0: continue
                if i > 0:
                    left = mat[i-1][j]
                else:
                    left = 10**999
                if j > 0:
                    up = mat[i][j-1]
                else:
                    up = 10**999
                mat[i][j] = min(up, left) + 1
        
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] == 0: continue
                if i < len(mat)-1:
                    right = mat[i+1][j]
                else:
                    right = 10**999
                if j < len(mat[0]) - 1:
                    down = mat[i][j+1]
                else:
                    down = 10**999
                    
                    
                mat[i][j] = min(min(right, down) + 1, mat[i][j])
        
        return mat
                