class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mDict = {}
                
        for s in magazine:
            if s not in mDict: mDict[s] = 1
            else: mDict[s]+=1
             
        print(mDict)
        
        for s in ransomNote:
            if s not in mDict or mDict[s]==0:
                return False
            else: mDict[s]-=1
                
        return True