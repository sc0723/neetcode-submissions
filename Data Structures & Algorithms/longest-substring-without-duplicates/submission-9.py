class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        used = set()
        longest = 0
        
        for j in range(len(s)):
            while s[j] in used:
                used.remove(s[i])
                i += 1

            used.add(s[j])
            
            longest = max(longest, (j - i) + 1)
        
        return longest