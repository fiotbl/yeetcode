class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 10**10
        left = 0
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1                
        return 0 if res == 10**10 else res
                