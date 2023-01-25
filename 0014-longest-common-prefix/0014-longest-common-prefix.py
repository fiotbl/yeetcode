class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for letter in zip(*strs):
            if len(set(letter)) == 1:
                res += letter[0]
            else:
                return res
        
        return res