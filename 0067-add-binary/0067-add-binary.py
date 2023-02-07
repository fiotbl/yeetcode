class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a = "0"*(len(b)-len(a))+a
        else:
            b = "0"*(len(a)-len(b))+b
            
        carry = 0
        res = ""
        
        for i in range(len(a)-1, -1, -1):
            total = carry + int(a[i]) + int(b[i])
            value = total % 2
            carry = total // 2
            res =  str(value) + res
            
        if carry == 1: res = "1"+res 
        return res