class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []
        
        for i in points:
            dist = i[0]**2 + i[1]**2
            h.append((dist, i))
        
        heapq.heapify(h)
        
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
            
        return res