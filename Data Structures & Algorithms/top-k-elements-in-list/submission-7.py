import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        print(freq)
        
        for n, occ in freq.items():
            heap.append((-1 * occ, n))
        heapq.heapify(heap)
        print(heap)
        result = []
        for i in range(k):
            count, val = heapq.heappop(heap)
            result.append(val)
        return result


