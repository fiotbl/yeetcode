class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count, res = 0, nums[0]
        
        for num in nums:
            if count < 0:
                count = 0
            count += num
            res = max(res, count)
            
        return res