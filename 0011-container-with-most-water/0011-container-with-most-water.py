class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l<r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        
        
#         res = 0
        
#         for i in range(len(height)):
#             for j in range (i+1, len(height)):
#                 res = max(res, (j-i)*min(height[i], height[j]))
                
#         return res
            