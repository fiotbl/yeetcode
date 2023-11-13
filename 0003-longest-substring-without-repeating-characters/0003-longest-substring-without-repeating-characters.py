class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        lst = []
        
        for letter in s:
            while letter in lst:
                lst.pop(0)
                l += 1
            lst.append(letter)
            length = max(length, len(lst))
                
        return length