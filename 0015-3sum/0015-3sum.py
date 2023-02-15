class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: # i > 0 for example case of [0,0,0]
                continue
            target = 0 - num
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        
        return res
                    
                    
                    
            