class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskDict = {e:tasks.count(e) for e in set(tasks)}
        maxHeap = [-count for count in taskDict.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        queue = []
        
        while maxHeap or queue:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt < 0:
                    queue.append((cnt, time + n))
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.pop(0)[0])
                
        return time
            
        