class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        
        while r < len(prices):
            diff = prices[r] - prices[l]
            profit = max(profit, diff)
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return profit