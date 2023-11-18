class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        curr = l
        res = 0
        
        while l<r:
            total = min(maxL, maxR) - height[curr]
            res += total if total > 0 else 0
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            
            if height[l] < height[r]:
                l += 1
                curr = l
                # maxL = max(maxL, height[l])
            else:
                r -= 1
                curr = r
                # maxR = max(maxR, height[r])
            
        return res