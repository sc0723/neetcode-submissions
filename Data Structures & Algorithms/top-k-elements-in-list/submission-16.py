import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, value in freq.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            freq, val = heapq.heappop(heap)
            ans.append(val)
        
        return ans

