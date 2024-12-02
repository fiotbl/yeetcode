class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        
        def find(target):
            track = [0] * (len(nums) + 1)
            for query in queries[:target]:  # O(Q)
                track[query[0]] += query[2]
                track[query[1] + 1] -= query[2]

            for j in range(1, len(track)):  # O(n)
                track[j] += track[j-1]

            for i, num in enumerate(nums): # O(n)
                if track[i] < num:
                    return False

            return True
        
        l, r = 0, len(queries) + 1
        
        while l<r:
            mid = (l+r)//2
            if find(mid):
                r = mid 
            else:
                l = mid + 1
                
        if l > len(queries): return -1
        return l