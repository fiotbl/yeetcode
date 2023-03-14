class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs,  pre in prerequisites:
            preMap[crs].append(pre)
            
        visitedCourses = set()

        def dfs(crs):
            if crs in visitedCourses: 
                return False
            if preMap[crs] == []: 
                return True
            
            visitedCourses.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitedCourses.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True