class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = { 0 : 1}
        currSum = 0 
        res = 0
        
        for n in nums:
            currSum += n
            remainder = currSum % k
            res += prefixSum.get(remainder, 0)
            prefixSum[remainder] = prefixSum.get(remainder, 0) + 1

        
        return res