class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, a, b = 0, 0, 1
        
        if len(prices) == 0: return res
        
        while b < len(prices):
            diff = prices[b] - prices[a]
            if diff > res:
                res = diff
            elif prices[b] < prices[a]:
                a = b
            b += 1
        
        return res