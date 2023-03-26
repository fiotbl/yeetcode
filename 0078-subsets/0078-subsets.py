class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include the curr num
            dfs(i+1)
            subset.append(nums[i])
            dfs(i+1)
            
            # don't include the curr num
            subset.pop()
            
        dfs(0)
        return res