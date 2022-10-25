class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alphaDict = dict(zip(range(1,27), string.ascii_lowercase))
        currK = k   
        maxValue = 26
        res = ""
        while(n > 0):
            if currK == n:
                res = n*"a" + res
                break
            if (currK - maxValue) < (n-1):
                maxValue -= 1
                continue
            res = alphaDict[maxValue] + res
            n -= 1
            currK = currK - maxValue
            maxValue = 26
        return res

