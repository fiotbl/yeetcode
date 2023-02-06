class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueSet = set()
        left = 0
        res = 0
        
        for right in range(len(s)):
            while s[right] in uniqueSet:
                uniqueSet.remove(s[left])
                left+=1
            uniqueSet.add(s[right])
            res = max(res, right-left+1)
            
        return res