class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        
        for letter in s:
            if letter not in sDict:
                sDict[letter] = 1
            else:
                sDict[letter] += 1
        
        for letter in t:
            if letter not in tDict:
                tDict[letter] = 1
            else:
                tDict[letter] += 1
                
                
        return sDict == tDict