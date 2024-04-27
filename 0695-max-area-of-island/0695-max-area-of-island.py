class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = []
        
        def bfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i,j) in visited: return 0    
            visited.append((i,j))
            return 1 + bfs(i-1,j) + bfs(i+1,j) + bfs(i,j-1) + bfs(i, j+1)
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, bfs(i,j))
        
        return res