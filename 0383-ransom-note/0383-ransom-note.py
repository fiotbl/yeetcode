class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mDict = {e:magazine.count(e) for e in set(magazine)}
        
        for letter in ransomNote:
            if letter in mDict and mDict[letter]!=0:
                mDict[letter] -= 1
            else:
                return False
        
        return True