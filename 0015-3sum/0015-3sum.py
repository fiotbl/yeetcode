class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            target = 0 - num
            l, r = i + 1, len(nums)-1
            while l<r:
                total = nums[l] + nums[r]
                if total > target:
                    r-=1
                elif total < target:
                    l+=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res
            
        
        