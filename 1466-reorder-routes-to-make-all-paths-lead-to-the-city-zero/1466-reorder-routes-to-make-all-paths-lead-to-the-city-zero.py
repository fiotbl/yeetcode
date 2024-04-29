class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        maps = {i:[] for i in range(n)}
        
        for i, j in connections:
            maps[i].append(j)
            maps[j].append(i)
        
        connections1 = { (i,j) for i,j in connections}
        visited = set()
        def dfs(i):
            for n in maps[i]:
                if n in visited: continue
                if (n,i) not in connections1:
                    nonlocal res
                    res +=1
                visited.add(i)
                dfs(n)
        visited.add(0)
        dfs(0)
        return res
            