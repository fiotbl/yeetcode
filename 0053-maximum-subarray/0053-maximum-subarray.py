class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxValue = max(maxValue, currSum)

        return maxValue