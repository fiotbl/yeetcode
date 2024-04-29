class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        def search(nums):
            if len(nums) < 3: return max(nums)
            nums[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                nums[i] = max(nums[i-1], nums[i] + nums[i-2])

            return nums[len(nums)-1]
        
        return max(search(nums[1:]), search(nums[:len(nums)-1]))