class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        i = 0
        
        while i<=r:
            if nums[i] == 2:
                tmp = nums[r] 
                nums[r] = 2
                nums[i] = tmp
                r -= 1
                i -= 1
            elif nums[i] == 0:
                tmp = nums[l] 
                nums[l] = 0
                nums[i] = tmp
                l += 1
            i += 1
            
            