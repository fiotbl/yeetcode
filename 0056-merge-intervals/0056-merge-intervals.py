class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        
        for interval in intervals:
            lastEnd = res[-1][1]
            if lastEnd >= interval[0]:
                res[-1][1] = max(lastEnd, interval[1])
            else:
                res.append(interval)
                
        return res
            