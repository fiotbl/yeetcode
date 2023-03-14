class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        
        for token in tokens:
            if token in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                res = eval(str(num2) + token + str(num1))
                stack.append(int(res))
            else:
                stack.append(token)
        
        return int(stack[0])