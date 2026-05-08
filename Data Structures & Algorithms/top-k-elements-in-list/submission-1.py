class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import heappush, heappop

        frequency_map = Counter(nums)
        max_heap = []

        for key, value in frequency_map.items():
            heappush(max_heap, (-value, key))
        
        result = []
        while k:
            _, num = heappop(max_heap)
            result.append(num)
            k-=1
        
        return result