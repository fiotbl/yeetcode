class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l, r = 0, 0
        lst = []
        
        while r < len(s):
            if s[r] not in lst:
                lst.append(s[r])
                r += 1
                # length = len(lst)
            else:
                print(lst)
                # length = max(length, len(lst))
                while s[r] in lst:
                    l += 1
                    lst.pop(0)
                lst.append(s[r])
                r = r+1
            length = max(length, len(lst))
                
        return length