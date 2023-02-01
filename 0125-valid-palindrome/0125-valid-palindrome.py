class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = []
        
        for letter in s:
            if letter.isalnum():
                news.append(letter.lower())
              
        print(news)
        l, r = 0, len(news)-1
        
        while l<=r:
            if news[l]!=news[r]: return False
            l, r = l+1, r-1
            
        return True