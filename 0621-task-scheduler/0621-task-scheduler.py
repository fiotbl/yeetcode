class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = []
        counts = Counter(tasks)
        heap1 = [-count for count in counts.values()]
        heapq.heapify(heap1)
        time = 0

        while queue or heap1:
            time += 1
            
            if heap1:
                cnt = 1 + heapq.heappop(heap1)
                if cnt < 0:
                    queue.append([cnt, time + n])
            
            if queue and time == queue[0][1]:
                heapq.heappush(heap1, queue.pop(0)[0])
        
        return time