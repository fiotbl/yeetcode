class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = { num : index for index, num in enumerate(nums)}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in d and d[remainder]!=i:
                res = []
                res.extend([i, d[remainder]]) 
                return res