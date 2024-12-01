class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Line sweep
        track = [0] * (len(nums) + 1)
        
        for query in queries:  # O(Q)
            track[query[0]] += 1
            track[query[1] + 1] -= 1

        for j in range(1, len(track)):  # O(n)
            track[j] += track[j-1]

        for i, num in enumerate(nums): # O(n)
            if track[i] < num:
                return False
            
        return True