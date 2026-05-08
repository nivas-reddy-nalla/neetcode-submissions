from _heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        l, r = 0, k
        result = []

        for i in range(r):
            heappush(max_heap, (-nums[i], i))
        result.append(-max_heap[0][0])
        l+=1
        for i in range(r, len(nums)):
            heappush(max_heap, (-nums[i], i))

            while max_heap[0][1]<l:
                heappop(max_heap)

            val, _ = max_heap[0]
            result.append(-val)
            l+=1
        return result

            

            