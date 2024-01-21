class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i , temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][1]:
                j, temp2 = stack.pop()
                res[j] = i-j
            stack.append([i, temp])
        
        return res