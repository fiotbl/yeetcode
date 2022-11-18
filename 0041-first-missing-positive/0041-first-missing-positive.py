class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        uniqueSet = set(nums)
        print(type(uniqueSet))
        i = 1
        while i in uniqueSet:
            i+=1
        return i
                
        
        
        