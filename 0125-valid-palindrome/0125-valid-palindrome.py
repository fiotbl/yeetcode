class Solution:
    def isPalindrome(self, s: str) -> bool:

        news = "".join(ch.lower() for ch in s if ch.isalnum())
        l, r = 0, len(news)-1

        while l<=r:
            if news[l]!=news[r]: return False
            l, r = l+1, r-1
            
        return True