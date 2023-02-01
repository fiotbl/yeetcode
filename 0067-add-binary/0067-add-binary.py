class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b): b = "0"*(len(a)-len(b)) + b
        else: a = "0"*(len(b)-len(a)) + a
        
        res, carry = [], False

        for i in range(len(a) - 1, -1, -1):
            if carry:
                bitsum = int(a[i]) + int(b[i]) + 1
                carry = False
            else:
                bitsum = int(a[i]) + int(b[i])
            if bitsum == 2:
                carry = True
                res.append(0)
            elif bitsum ==3:
                carry = True
                res.append(1)
            else: res.append(bitsum)
                
        if carry: res.append(1) 
        return "".join(str(a) for a in res[::-1] )