class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {0:0}
        
        for w in wall:
            curr = 0
            for brick in w[:-1]:
                curr += brick
                gaps[curr] = 1 + gaps.get(curr, 0)
        return len(wall) - max(gaps.values())