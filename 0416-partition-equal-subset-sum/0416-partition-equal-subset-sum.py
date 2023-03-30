class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = sum(nums) // 2
        
        sums = set()
        sums.add(0)
        
        for num in nums:
            tmp = set()
            for t in sums:
                if num + t == target: return True
                tmp.add(t)
                tmp.add(t+num)
            sums = tmp
        return False