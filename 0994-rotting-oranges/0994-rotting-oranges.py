class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
          
        dirs = [[1, 0], [0, 1], [-1,0], [0, -1]]
        while q and fresh > 0:
            lenQ = len(q)
            for i in range(lenQ):
                r, c = q.pop(0)
                for dirR, dirC in dirs:
                    r1, c1 = r + dirR, c + dirC
                    if r1 in range(len(grid)) and c1 in range(len(grid[0])) and grid[r1][c1] == 1:
                        grid[r1][c1] = 2
                        fresh -= 1
                        q.append((r1,c1))
            time += 1
        
        return time if fresh == 0 else -1
                