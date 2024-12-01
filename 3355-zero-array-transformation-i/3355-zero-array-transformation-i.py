class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        track = [0] * (len(nums) + 1)
        
        for query in queries:
            track[query[0]] += 1
            track[query[1] + 1] -= 1

        for j in range(1, len(track)):
            track[j] += track[j-1]

        for i, num in enumerate(nums):
            if track[i] < num:
                return False
            
        return True