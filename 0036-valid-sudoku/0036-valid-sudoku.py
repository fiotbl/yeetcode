class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        sq = collections.defaultdict(list)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sq[(r//3, c//3)]:
                    return False
                row[r].append(board[r][c])
                col[c].append(board[r][c])
                sq[(r//3, c//3)].append(board[r][c])
        
        return True