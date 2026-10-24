class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for s in num_set:
            if s - 1 not in num_set:
                curr = 1
                while s + 1 in num_set:
                    curr += 1
                    s += 1
                    
                longest = max(longest, curr)
        
        return longest