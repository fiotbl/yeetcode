class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(ch.lower() for ch in s if ch.isalnum())
                
        l, r = 0, len(new) - 1
        
        while(l<r):
            if new[l] != new[r]: return False
            l, r = l+1, r-1
        
        return True