class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index, visited):
            if index == len(word):
                return True
            if i<0 or i>len(board)-1: return False
            if j<0 or j>len(board[0])-1: return False
            if board[i][j] != word[index]: return False
            if (i,j) in visited: return False
            
            visited.add((i,j))
            res = dfs(i,j-1,index+1,visited) or dfs(i-1,j,index+1,visited) or dfs(i+1,j,index+1,visited) or dfs(i,j+1,index+1,visited)
            visited.remove((i,j))
            
            return res
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0,visited): return True
                
        return False