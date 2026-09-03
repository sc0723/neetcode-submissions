from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = Counter(s)

        for c in t:
            if c in s_freq:
                s_freq[c] -= 1
                if s_freq[c] < 0:
                    return False
            else:
                return False
        
        return True
            