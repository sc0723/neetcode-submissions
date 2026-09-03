class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ""
        for c in s.lower():
            if c.isalnum():
                processed += c
        
        i = 0
        j = len(processed) - 1

        while i <= j:
            if processed[i] != processed[j]:
                return False
            i += 1
            j -= 1
        
        return True