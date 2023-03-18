class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0" or (i,j) in visitedSet: return 

            visitedSet.add((i,j))

            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        islands = 0
        visitedSet = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visitedSet:
                    dfs(grid, i, j)
                    islands += 1

        return islands
    
