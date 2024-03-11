class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        curr = ""
        
        def backtrack(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            
            letters = letterMap[digits[i]]
            for j in range(len(letters)):
                curr += letters[j]
                backtrack(i+1, curr)
                curr = curr[:-1]
        
        if not digits:
            return []
        
        backtrack(0,"")
        return res