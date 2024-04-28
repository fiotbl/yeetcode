class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = {i: [] for i in range(numCourses)}
        for prereq, course in prerequisites:
            maps[prereq].append(course)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if maps[course] == []:
                return True
            
            visited.add(course)
            for prereq in maps[course]:
                if not dfs(prereq): return False
            maps[course] = []
            visited.remove(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
        