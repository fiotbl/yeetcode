class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        letters = []
        res = 0
        
        for j in range(len(s)):
            while s[j] in letters:
                letters.pop(0)
                i += 1
            letters.append(s[j])
            res = max(res, len(letters))
            
        return res
            