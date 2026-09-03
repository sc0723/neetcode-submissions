class Solution:
    def isPalindrome(self, s: str) -> bool:

        processed_str = ""

        for c in s.lower():
            if c.isalnum():
                processed_str += c
        
        i, j = 0, len(processed_str) - 1

        while i <= j:
            if processed_str[i] != processed_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
