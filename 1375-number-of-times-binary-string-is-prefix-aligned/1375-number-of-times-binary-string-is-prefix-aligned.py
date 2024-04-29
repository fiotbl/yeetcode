class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0 
        rightMostFlipped = 0
        count = 0
        
        for i, flip in enumerate(flips):
            rightMostFlipped = max(rightMostFlipped, flip)
            count += 1
            
            if count == rightMostFlipped:
                res += 1
                
        return res