class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, total = nums[0], 0
        
        for num in nums:
            total += num
            res = max(res, total)
            if total < 0: total = 0
            
        return res
    
    
    
#         maxValue = nums[0]
#         currSum = 0
        
#         for num in nums:
#             if currSum < 0:
#                 currSum = 0
#             currSum += num
#             maxValue = max(maxValue, currSum)

#         return maxValue