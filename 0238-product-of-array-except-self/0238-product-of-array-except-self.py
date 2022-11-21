class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        value = 1
        res = []
        for i in range(len(nums)):
            res.append(value)
            value *= nums[i]
        
        value = 1
            
        for i in reversed(range(len(nums))):
            res[i] *= value
            value *= nums[i]
            
        return res
        
        