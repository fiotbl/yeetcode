class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        
        for s in strs:
            lst = [0] * 26
            for letter in s:
                lst[ord(letter)-97] += 1
            dic[tuple(lst)].append(s)
            
        return dic.values()