# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        l, r = 1, n
        
        while l<=r:
            mid = (l + r) // 2
            ver = isBadVersion(mid)
            if not ver:
                l = mid + 1
            if ver:
                r = mid - 1
        return l
            