import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        heap = []
        for val, occ in freq.items():
            heap.append((-1 * occ, val))
        
        heapq.heapify(heap)
        res = []
        for i in range(k):
            o, v = heapq.heappop(heap)
            res.append(v)
        return res

