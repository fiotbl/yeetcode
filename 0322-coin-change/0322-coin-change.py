class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [amount + 1] * (amount + 1) 
        counts[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    counts[a] = min(counts[a], 1 + counts[a-c])
                    
        return counts[amount] if counts[amount] != amount + 1 else -1