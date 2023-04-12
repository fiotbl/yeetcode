class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = []
        tasksDict = {e:tasks.count(e) for e in set(tasks)}
        counts = [-count for count in tasksDict.values()]
        heapq.heapify(counts)
        
        time = 0
        
        while counts or queue:
            time += 1
            
            if counts:
                cnt = 1 + heapq.heappop(counts)
                if cnt < 0:
                    queue.append((cnt, time+n))
            
            if queue and time == queue[0][1]:
                heapq.heappush(counts, queue.pop(0)[0])
                
        return time