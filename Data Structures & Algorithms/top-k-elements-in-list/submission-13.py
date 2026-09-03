import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for n, count in freq.items():
            heap.append((-count, n))
        
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            c, n = heapq.heappop(heap)
            res.append(n)

        return res