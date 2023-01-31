class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0
        
        for n in nums:
            if n!= res and count > 0: 
                count -= 1
            elif n != res and count == 0: 
                res = n
            else: count += 1
                
        return res