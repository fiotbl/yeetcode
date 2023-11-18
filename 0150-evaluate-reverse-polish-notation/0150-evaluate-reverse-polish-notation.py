class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                v1 = stack.pop()
                v2 = stack.pop()
                if token == '+': ans = v2 + v1
                elif token == '-': ans = v2 - v1
                elif token == '*': ans = v2 * v1
                elif token == '/': ans = int(v2/v1)
                stack.append(ans)
            else:
                stack.append(int(token))
        
        return stack[0]