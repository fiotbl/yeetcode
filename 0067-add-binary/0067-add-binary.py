class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else: 
            b = "0" * (len(a) - len(b)) + b
        
        res, carry, total = "", 0, 0
        
        for i in range(len(a)-1, -1, -1):
            total = (carry + int(a[i]) + int(b[i])) % 2
            carry = (carry + int(a[i]) + int(b[i])) // 2
            res = str(total) + res
        
        return "1"+res if carry==1 else res