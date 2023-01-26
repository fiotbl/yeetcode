class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = { "(" : ")",
               "{" : "}",
               "[" : "]"}
        
        stack = []

        for i in s:
            if i in bracketDict:
                stack.append(bracketDict[i])
            elif len(stack) == 0 or stack[-1] != i:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = { "(" : ")",
#             "[" : "]",
#             "{": "}"}
#         stack = []
        
#         for i in s:
#             if i in d:
#                 stack.append(d[i])
#             elif not stack or stack[-1]!=i:
#                 return False
#             else:
#                 stack.pop()
                
#         return len(stack)==0