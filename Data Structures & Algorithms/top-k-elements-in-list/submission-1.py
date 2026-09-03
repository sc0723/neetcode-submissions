from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        heap = []

        for n, occ in freq.items():
            heap.append((-1 * occ, n))
        
        heapq.heapify(heap)
        result = []
        for i in range(k):
            counter, value = heapq.heappop(heap)
            result.append(value)
        return result