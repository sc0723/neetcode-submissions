class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for s in s.lower():
            if s.isalnum():
                new += s
        return new == new[::-1]



        