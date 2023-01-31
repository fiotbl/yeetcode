class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {e:nums.count(e) for e in set(nums)}
        
        return max(numsDict, key = numsDict.get)