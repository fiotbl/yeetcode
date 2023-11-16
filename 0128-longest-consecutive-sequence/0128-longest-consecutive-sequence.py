class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        
        for num in nums:
            if (num-1) not in numSet:
                add = 0
                while (num + add) in numSet:
                    add += 1
                length = max(add, length)
            
        return length