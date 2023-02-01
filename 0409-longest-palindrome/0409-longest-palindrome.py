class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {e:s.count(e) for e in set(s)}
        count = 0
        
        for key in counts:
            if counts[key] >= 2:
                count += 2*(counts[key] // 2)
                counts[key] %= 2
                
        if 1 in counts.values(): count += 1
            
        return count