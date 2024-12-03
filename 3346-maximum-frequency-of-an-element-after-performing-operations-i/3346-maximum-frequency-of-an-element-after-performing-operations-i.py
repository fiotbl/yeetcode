class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        save = [0] * (max(nums)+1+k)
        
        for num in nums:
            save[num] += 1
        
        counts = [save[0]]
        
        for i in range(1, len(save)):
            counts.append(counts[i-1]+save[i])
        
        res = 0
        for i in range(len(counts)-k):                                                            
            l = max(0, i-k-1)
            r = min(len(counts)-1, i+k)
            numCounts = save[i]
            
            changes = counts[r] - counts[l] - numCounts
            if changes > numOperations:
                res = max(res, numOperations+numCounts)
            else:
                res = max(res, changes+numCounts)
            
        return res