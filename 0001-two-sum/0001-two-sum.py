class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = { num : index for index, num in enumerate(nums)}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d and i != d[diff]:
                return [i, d[diff]]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = { num : index for index, num in enumerate(nums)}
        
#         for i in range(len(nums)):
#             remainder = target - nums[i]
#             if remainder in d and d[remainder]!=i:
#                 return [i, d[remainder]]