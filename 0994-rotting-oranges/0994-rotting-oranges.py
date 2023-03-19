class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        rotten = []
        count = 0
        fresh = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        directions = [[0, 1], [0, -1], [1,0], [-1,0]]
        while rotten and fresh > 0:
            print(rotten)
            count += 1
            rottenLen = len(rotten)
            for i in range(rottenLen):
                row, col = rotten.pop(0)
                for dr, dc in directions:
                    r, c = dr+row, dc+col
                    if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] == 0  or grid[r][c] == 2: continue
                    grid[r][c] = 2
                    rotten.append((r,c))      
                    fresh -= 1
            

        return -1 if fresh > 0 else count