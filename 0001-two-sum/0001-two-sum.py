class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictNums = {k: v for v, k in enumerate(nums)}
        dictNums = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in dictNums: return [i, dictNums[value]]
            dictNums[num] = i