class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = 100000
        while l<=r:
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[mid]<nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res