class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0"*(len(b) - len(a)) + a
        else:
            b = "0"*(len(a) - len(b)) + b
            
        carry = 0
        res = ""
        for i in range(len(a)-1,-1,-1):
            addition = carry + int(a[i]) + int(b[i])
            ans = addition % 2
            carry = addition // 2
            res = str(ans) + str(res)
            
        return res if carry == 0 else "1"+res
            