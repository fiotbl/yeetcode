class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][1]:
                j, tempz = stack.pop()
                res[j] = i - j
            stack.append([i, temp])
        return res
                