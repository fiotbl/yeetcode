class Solution:
    def isValid(self, s: str) -> bool:
        d = { "(" : ")",
            "[" : "]",
            "{": "}"}
        stack = []
        
        for i in s:
            if i in d:
                stack.append(d[i])
            elif not stack or stack[-1]!=i:
                return False
            else:
                stack.pop()
                
        return len(stack)==0