class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        
        stack = []
        
        for i in s:
            if i in dict:
                stack.append(dict[i])
            elif len(stack)==0 or stack[-1] != i:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0
                    