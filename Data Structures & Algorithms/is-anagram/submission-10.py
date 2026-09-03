class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        for char in t:
            if char in freq:
                freq[char] -= 1
                if freq[char] < 0:
                    return False
            else:
                return False
            
        return True