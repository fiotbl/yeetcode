class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i, j, m, visited):
            if m == len(word):return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in visited or word[m]!=board[i][j]: return False

            visited.add((i,j))
            res = (search(i-1,j,m+1,visited) or search(i+1,j,m+1,visited) or search(i,j+1,m+1,visited) or search(i,j-1,m+1,visited))
            visited.remove((i,j))
                
            return res
        
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j,0,visited): return True
                
        return False
            
            
            