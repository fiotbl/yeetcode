class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        l = 0
        
        for i in range(len(s1)-1, len(s2)):
            if s1Count == Counter(s2[l:i+1]):
                return True
            l += 1
        return False