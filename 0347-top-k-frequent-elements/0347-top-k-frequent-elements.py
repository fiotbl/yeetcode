class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        h = []
        res = []
        for key in dic:
            heapq.heappush(h, (dic[key], key))
        
        temp = heapq.nlargest(k, h)
        for i in temp:
            res.append(i[1])
        return res