class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        while l <= r:
            row = (l+r)//2
            print(row)
            if matrix[row][0] > target: r = row-1
            elif matrix[row][-1] < target: l = row+1
            else: break
        
        if l > r: return False
                
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] == target: return True
            if matrix[row][mid] > target: right = mid-1
            elif matrix[row][mid] < target: left = mid+1
        
        return False