class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        values = []
        for point in points:
            dist = (point[0])**2 + (point[1])**2
            values.append((dist, [point[0], point[1]]))
        
        heapq.heapify(values)
        
        res=[]
        
        for _ in range(k):
            res.append(heapq.heappop(values)[1])
            
        return res