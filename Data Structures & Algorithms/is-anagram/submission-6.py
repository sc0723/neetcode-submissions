class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        
        for y in t:
            if y in freq:
                freq[y] -= 1
                if freq[y] < 0:
                    return False
            else:
                return False
        
        return True