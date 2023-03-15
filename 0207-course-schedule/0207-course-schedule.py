class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        visitedCourses = []
        
        def dfs(course):
            print("course", course)
            if course in visitedCourses: return False
            if preMap[course] == []: 
                print("empty prereqs")
                return True
            
            visitedCourses.append(course)
            for crs in preMap[course]:
                print(course, "has a prereq of" , crs)
                if not dfs(crs): return False
            print("course", course)
                
            print("checked all its decendents")
            visitedCourses.remove(course)
            preMap[course] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
            
        return True
            
            
        
        