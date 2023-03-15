class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target: return mid
            
            # first check if left side if the strictly increasing side
            
            if nums[mid] >= nums[l]:
                if nums[mid] >= target and nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1