class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left = 0, 0
        uniqueValues = set()
        
        for right in range(len(s)):
            while s[right] in uniqueValues:
                uniqueValues.remove(s[left])
                left += 1
            uniqueValues.add(s[right])
            res = max(res, right-left+1)
        return res