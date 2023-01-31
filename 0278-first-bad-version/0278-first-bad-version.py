# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        badVer = 0
        
        while l<=r:
            mid = (l+r) // 2
            print(mid)
            if isBadVersion(mid):
                r = mid-1
                badVer = mid
                print(badVer)
            else:
                l=mid+1
                
        return badVer