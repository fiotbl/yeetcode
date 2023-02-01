class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        if lena > lenb:
            b = "0"*(lena-lenb) + b
        else:
            a = "0"*(lenb-lena) + a
        
        res = []
        carry = False
        print(lena)
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
            print(res) 
        
        if carry: res.append(1)
        ans = res[::-1]     
        return "".join(str(a) for a in ans)