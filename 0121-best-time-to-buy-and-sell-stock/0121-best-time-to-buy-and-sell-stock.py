class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res= 0
        
        while r<len(prices):
            diff = prices[r]-prices[l]
            if diff > res: res = diff
            if prices[r] < prices[l]:
                l = r
            r+=1
        return res