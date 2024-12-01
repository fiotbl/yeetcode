class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        track = [0] * (len(nums) + 1)
        
        for query in queries:
            track[query[0]] += 1
            track[query[1] + 1] -= 1
        print(track)
        for j in range(1, len(track)):
            print(track[j])
            print(track[j-1])
            print("--")
            track[j] += track[j-1]
        
        print(track)
        for i, num in enumerate(nums):
            if track[i] < num:
                return False
            
        return True