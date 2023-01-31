class Solution:
    def longestPalindrome(self, s: str) -> int:
        sDict = {e:s.count(e) for e in set(s)}
        count = 0
        
        for letter in sDict:
            if sDict[letter]>=2:
                while sDict[letter]>1:
                    count += 2
                    sDict[letter] -= 2
        
        for letter in sDict:
            if sDict[letter]==1:
                count += 1
                break
                
        return count