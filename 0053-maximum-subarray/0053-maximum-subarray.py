class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, total = -999999, 0
        
        if len(nums) == 1: return nums[0]
        for num in nums:
            total += num
            if total > res: res = total
            if total < 0: total = 0
            
        return res