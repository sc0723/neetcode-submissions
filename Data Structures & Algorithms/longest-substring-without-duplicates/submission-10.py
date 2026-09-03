class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_window = set()

        i = 0
        for j in range(len(s)):
            while s[j] in current_window:
                current_window.remove(s[i])
                i += 1
            
            current_window.add(s[j])
            max_length = max(max_length, j - i + 1)
        
        return max_length