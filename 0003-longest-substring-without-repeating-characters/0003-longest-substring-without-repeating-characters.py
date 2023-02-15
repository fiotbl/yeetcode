class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueSet = set()
        res, left = 0, 0
        left = 0
        
        for letter in s:
            while letter in uniqueSet:
                uniqueSet.remove(s[left])
                left += 1
            uniqueSet.add(letter)
            res = max(res, len(uniqueSet))
            
        return res