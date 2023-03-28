class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, curString, m):
            # print(curString)
            if curString == word: return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in visited or board[i][j] != word[m]: return False
            if board[i][j] == word[m]:
                visited.add((i,j))
                m += 1
                curString += (board[i][j])
                res = dfs(i-1, j, curString, m) or dfs(i+1, j, curString,  m) or dfs(i, j+1, curString,  m) or dfs(i, j-1, curString, m)
                visited.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, "", 0):
                    return True
        return False
            
            
            