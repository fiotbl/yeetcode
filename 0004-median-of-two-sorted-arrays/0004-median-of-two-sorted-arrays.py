class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        
        while True:
            mid = (l+r) // 2
            j = half - mid - 2
            
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if (mid + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Bleft, Aleft) + min(Bright, Aright)) / 2
                else:
                    return (min(Bright, Aright))
            
            if Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1