class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0
        
        def find(target):
            track = [0] * (len(nums) + 1)
            for query in queries[:target+1]:  # O(Q)
                track[query[0]] += query[2]
                track[query[1] + 1] -= query[2]

            for j in range(1, len(track)):  # O(n)
                track[j] += track[j-1]

            for i, num in enumerate(nums): # O(n)
                if track[i] < num:
                    return False

            return True
        
        l, r = 0, len(queries) 
        res = 0
        while l<=r:
            mid = (l+r)//2
            if find(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        if l > len(queries): return -1
        return l+1