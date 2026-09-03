from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = Counter(s)

        for c in t:
            if c in freq_s:
                freq_s[c] -= 1
                if freq_s[c] < 0:
                    return False
            else:
                return False
            
        return True

        