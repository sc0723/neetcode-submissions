class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_window = set()
        max_string = 0

        i = 0
        for j in range(len(s)):
            while s[j] in curr_window:
                curr_window.remove(s[i])
                i += 1
            curr_window.add(s[j])
            max_string = max(max_string, j - i + 1)
        
        return max_string
