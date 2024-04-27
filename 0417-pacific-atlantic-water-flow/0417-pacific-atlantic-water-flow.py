class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        alt = set()
        
        def bfs(i,j,visited,prevHeight):
            if (i,j) in visited or i < 0 or j < 0 or i ==len(heights) or j == len(heights[0]) or heights[i][j] < prevHeight: return 
            
            visited.add((i,j))
            bfs(i-1,j,visited,heights[i][j])
            bfs(i+1,j,visited,heights[i][j])
            bfs(i,j-1,visited,heights[i][j])
            bfs(i,j+1,visited,heights[i][j])
            
        for i in range(COLS):
            bfs(0,i,pac,heights[0][i])
            bfs(ROWS-1,i,alt,heights[ROWS-1][i])
            
        for i in range(ROWS):
            bfs(i,0,pac,heights[i][0])
            bfs(i,COLS-1,alt,heights[i][COLS-1])
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in alt and (i,j) in pac:
                    res.append([i,j])
        
        return res
        