class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        res = []
        
        for i, point in enumerate(points):
            dist = ((point[0] - 0)**2 + (point[1] - 0)**2 )**0.5
            distances[i] = dist
        
        sortedDistances = sorted(distances.items(), key=lambda x: x[1])

        for key in sortedDistances:
            if k == 0: break
            res.append(points[key[0]])
            k-=1
            
        return res
        
        