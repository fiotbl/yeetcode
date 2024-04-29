class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        maps = {i:[] for i in range(1, len(edges)+1)}
        
        for i, j in edges:
            maps[i].append(j)
            maps[j].append(i)
        
    
        def isTree(i, prev):
            
            if i in visited: return False
            
            visited.add(i)
            for j in maps[i]:
                if j == prev: continue
                if not isTree(j, i): return False
            
            return True
        
        res = []
        
        for i, j in edges:
            maps[i].remove(j)
            maps[j].remove(i)
            visited = set()

            if isTree(1, -1) and len(visited) == len(edges):
                res = [i,j]
            maps[i].append(j)
            maps[j].append(i)
        
        return res