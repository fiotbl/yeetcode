class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = []
        count = 0
        
        def rot(grid, i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == 0  or grid[i][j] == 2: return
            grid[i][j] = 2
            if (i,j) not in rotten:
                rotten.append((i,j))      
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        while rotten:
            count += 1
            rottenLen = len(rotten)
            for i in range(rottenLen):
                cell = rotten.pop(0)
                rot(grid, cell[0]-1, cell[1])
                rot(grid, cell[0]+1, cell[1])
                rot(grid, cell[0], cell[1]-1)
                rot(grid, cell[0], cell[1]+1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return count-1 if count>0 else 0