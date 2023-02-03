class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, currSum = nums[0], 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            res = max(res, currSum)
            
        return res