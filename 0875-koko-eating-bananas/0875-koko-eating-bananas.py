class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l<=r:
            mid = (l+r)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            print(total)
            if total <= h: 
                res = mid
                r = mid-1
            elif total > h: l = mid+1
        
        return res