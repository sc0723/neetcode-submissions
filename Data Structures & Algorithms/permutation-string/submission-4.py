from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = Counter(s1)
        s2_freq = defaultdict(int)  # avoids the if/else
        matches = 0
        l = 0
        target = len(s1_freq)  # number of unique chars to match

        for r in range(len(s2)):
            # Add right character
            char = s2[r]
            if char in s1_freq:
                s2_freq[char] += 1
                # If count now matches, increment matches
                if s2_freq[char] == s1_freq[char]:
                    matches += 1
                # If count was one more than s1_freq before increment, decrement matches
                elif s2_freq[char] == s1_freq[char] + 1:
                    matches -= 1

            # Shrink window if it's bigger than s1
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in s1_freq:
                    # If count was exactly matching, now it will be off
                    if s2_freq[left_char] == s1_freq[left_char]:
                        matches -= 1
                    # If count was one more than target before decrement, now it matches
                    elif s2_freq[left_char] == s1_freq[left_char] + 1:
                        matches += 1
                    s2_freq[left_char] -= 1
                l += 1

            # Check if all matches are satisfied
            if matches == target:
                return True

        return False