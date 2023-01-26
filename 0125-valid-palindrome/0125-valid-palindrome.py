class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        
        for character in s:
            if character.isalnum():
                string.append(character.lower())
        
        
        l, r = 0, len(string)-1
        
        while l<r:
            if string[l] != string[r]:
                return False
            l, r = l+1, r-1
            
        return True
        