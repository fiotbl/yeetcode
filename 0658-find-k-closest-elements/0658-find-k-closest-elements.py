class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def binarySearch():
            l, r = 0, len(arr) - 1
            while l<r:
                mid = (l+r)//2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        pos = binarySearch()
        left, right = pos - 1, pos
        
        res = []
        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            else:
                if abs(x - arr[left]) <= abs(arr[right] - x):
                    print(arr[left])
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            k-=1
        
        return sorted(res)
        
        