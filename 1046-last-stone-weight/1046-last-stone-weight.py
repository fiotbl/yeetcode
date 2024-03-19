class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        stones = stones
        
        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            secondLargest = -heapq.heappop(stones)
            if largest != secondLargest:
                diff = largest - secondLargest
                heapq.heappush(stones, -diff)
        
        return -stones[0] if stones else 0