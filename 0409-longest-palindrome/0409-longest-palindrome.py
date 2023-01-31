class Solution:
    def longestPalindrome(self, s: str) -> int:
        sDict = {e:s.count(e) for e in set(s)}
        count = 0
        
        for letter in sDict:
            if sDict[letter]>=2:
                count += 2*(sDict[letter]//2)
                sDict[letter] = sDict[letter] % 2
        
        if 1 in sDict.values(): count+=1
                
        return count