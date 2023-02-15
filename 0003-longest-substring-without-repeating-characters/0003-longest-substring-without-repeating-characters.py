class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueSet = set()
        res = 0
        left = 0
        
        for letter in s:
            while letter in uniqueSet:
                uniqueSet.remove(s[left])
                left += 1
            uniqueSet.add(letter)
            print(len(uniqueSet))
            res = max(res, len(uniqueSet))
            
        return res