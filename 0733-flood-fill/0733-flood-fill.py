class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        
        def floodFilling(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != startingColor: return
            
            image[x][y] = color
            
            floodFilling(x-1, y)
            floodFilling(x+1, y)
            floodFilling(x, y-1)
            floodFilling(x, y+1)
            
        floodFilling(sr, sc)
        
        return image
            
            
            