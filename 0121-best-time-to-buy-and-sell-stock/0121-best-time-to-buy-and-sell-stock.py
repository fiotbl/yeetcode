class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        
        l, r = 0, 1
        
        while r < len(prices):
            if prices[r] - prices[l] > curr:
                curr = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            r += 1
            
        return curr
        