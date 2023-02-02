class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {e:s.count(e) for e in set(s)}
        tDict = {e:t.count(e) for e in set(t)}       
        
        return sDict == tDict
