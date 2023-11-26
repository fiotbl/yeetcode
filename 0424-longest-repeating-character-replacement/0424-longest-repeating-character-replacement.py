class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while len(s[l:i+1]) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, len(s[l:i+1]))
        
        return res