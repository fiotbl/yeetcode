class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        length = len(s1)
        
        for i in range(0, len(s2)):
            if s2[i] in s1Count:
                s1Count[s2[i]] -= 1
            if i>= length and s2[i-length] in s1Count:
                s1Count[s2[i-length]] += 1
            if all([s1Count[count] == 0 for count in s1Count]):
                return True
            
        return False