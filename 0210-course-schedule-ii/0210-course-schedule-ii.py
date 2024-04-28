class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        maps = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            maps[course].append(prereq)
        
        res= []
        visited = set()
        cycle = set()
        def dfs(course): 
            if course in visited:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for prereq in maps[course]:
                if not dfs(prereq): return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
            
        return res