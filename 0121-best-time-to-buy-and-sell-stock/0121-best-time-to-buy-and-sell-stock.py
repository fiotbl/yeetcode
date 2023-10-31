class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        diff = 0
        
        while s < len(prices):
            if prices[s] - prices[b] > diff:
                diff = prices[s] - prices[b]
            if prices[s] < prices[b]:
                b = s
            s += 1
        
        return diff