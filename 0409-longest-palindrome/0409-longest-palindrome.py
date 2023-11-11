class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {e:s.count(e) for e in set(s)}
        count = 0
        
        for n in dic:
            count += (dic[n]//2) * 2
            dic[n] = dic[n] - (dic[n]//2) * 2
        print(dic)
            
        if 1 in dic.values(): count += 1
        print(dic)
        
        return count