class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            num = nums.pop()
            # print(nums)
            # nums = [num] + nums
            nums.insert(0,num)
        
        