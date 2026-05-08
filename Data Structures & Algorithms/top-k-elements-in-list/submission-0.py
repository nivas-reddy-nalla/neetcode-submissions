from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        frequency_map = Counter(nums)

        for num in frequency_map:
            heappush(max_heap, (-frequency_map[num], num))
        
        result = []
        while k:
            _, val = heappop(max_heap)
            result.append(val)
            k-=1
        
        return result