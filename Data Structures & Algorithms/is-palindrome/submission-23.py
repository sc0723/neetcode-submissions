class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ""
        for c in s.lower():
            if c.isalnum():
                new += c
        x, t = 0, len(new) - 1    
        while x <= t:
            if new[x] != new[t]:
                return False
            x += 1
            t -= 1
        
        return True