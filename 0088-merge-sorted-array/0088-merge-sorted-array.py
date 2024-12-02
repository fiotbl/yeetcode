class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        A, B = m-1, n-1
        
        for p in range(m+n-1, -1, -1):
            if B < 0:
                break
            if A >= 0 and nums2[B] < nums1[A]:
                nums1[p] = nums1[A]
                A -= 1
            else:
                nums1[p] = nums2[B]
                B -= 1
            