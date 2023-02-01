class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b): b = "0"*(len(a)-len(b)) + b
        else: a = "0"*(len(b)-len(a)) + a
        
        res, carry = [], 0

        for i in range(len(a) - 1, -1, -1):
            bitsum = int(a[i]) + int(b[i]) + carry
            res.append(bitsum % 2)
            if bitsum >=2: carry = 1
            else: carry = 0
                
        if carry==1: res.append(1) 
        return "".join(str(a) for a in res[::-1] )