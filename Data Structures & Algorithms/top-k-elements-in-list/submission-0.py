class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]] = 1
        
        sort_freq = dict(sorted(freq.items(), key = lambda x:x[1], reverse = True))
        print(sort_freq)
        return list(sort_freq)[:k]