class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {e:magazine.count(e) for e in set(magazine)}
        for i in ransomNote:
            if i not in dic: return False
            elif dic[i] == 0: return False
            else: dic[i] = dic[i] - 1
                
        return True