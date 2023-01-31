class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
                
        mDict = {e:magazine.count(e) for e in set(magazine)}
        
        for s in ransomNote:
            if s not in mDict or mDict[s]==0:
                return False
            else: mDict[s]-=1
                
        return True