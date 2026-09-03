class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        start = set()
        for n in check:
            if n-1 not in check:
                start.add(n)
        maxSeq = 0
        for n in start:
            curr = 1
            while n+1 in check:
                curr+=1
                n+=1
            maxSeq = max(maxSeq, curr)
        return maxSeq