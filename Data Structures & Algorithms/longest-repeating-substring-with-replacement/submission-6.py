class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_track = {}
        i = 0
        max_freq = 0
        res = 0
        for j in range(len(s)):
            char_track[s[j]] = 1 + char_track.get(s[j], 0)
            max_freq = max(max_freq, char_track[s[j]])

            while (j - i + 1) - max_freq > k:
                char_track[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        return res
        

