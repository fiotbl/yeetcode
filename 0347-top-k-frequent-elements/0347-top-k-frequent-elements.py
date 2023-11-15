class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {e:nums.count(e) for e in set(nums)}
        h = []
        for key in dic:
            heapq.heappush(h, tuple([-dic[key], key]))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
            
        return res