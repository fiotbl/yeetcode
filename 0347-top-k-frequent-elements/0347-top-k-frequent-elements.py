class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        h = []
        for key in dic:
            heapq.heappush(h, tuple([dic[key], key]))
        
        res = []
        # for _ in range(k):
        #     res.append(heapq.heappop(h)[1])
        
        tmp = heapq.nlargest(k, h)
        for i in tmp:
            res.append(i[1])
            
        return res