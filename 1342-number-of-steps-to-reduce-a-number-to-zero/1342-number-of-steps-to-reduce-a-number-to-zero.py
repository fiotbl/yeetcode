class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = num
        count = 0
        
        while res != 0:
            if res % 2 == 0:
                res = res // 2
                count += 1
            else: 
                res -= 1
                count += 1
        
        return count
            