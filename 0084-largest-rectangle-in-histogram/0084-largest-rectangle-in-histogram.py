class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                maxArea = max(maxArea, h * (i-index))
                start = index
            stack.append((start, height))
        
        while stack:
            index, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - index))
            
        return maxArea