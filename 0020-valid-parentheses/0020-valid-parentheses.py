class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"(":")",
                     "{":"}",
                     "[":"]"}
        stack = []
        
        for i in s:
            if i in dictionary:
                stack.append(dictionary[i])
            elif len(stack)==0 or i != stack[len(stack)-1]:
                return False
            else:
                stack.pop()
        
        return len(stack)==0
                