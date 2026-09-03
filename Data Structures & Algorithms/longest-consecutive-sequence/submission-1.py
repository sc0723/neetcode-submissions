class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        start_points = set()
        res = 0
        for n in nums:
            if n - 1 not in nums:
                start_points.add(n)
        
        for s in start_points:
            curr = 1
            while s + 1 in nums:
                curr += 1
                s += 1
            res = max(res, curr)
        
        return res