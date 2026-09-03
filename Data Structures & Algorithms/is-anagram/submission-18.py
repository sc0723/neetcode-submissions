from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        if len(s) != len(t):
            return False

        for c in s:
            if c not in s_freq:
                s_freq[c] = 1
            else:
                s_freq[c] += 1

        for c in t:
            if c not in s_freq:
                return False
            
            s_freq[c] -= 1
            if s_freq[c] < 0:
                return False
        
        return True