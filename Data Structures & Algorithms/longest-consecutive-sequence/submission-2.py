class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        seen = set(nums)
        for num in nums:
            cur, count = num, 1
            while cur + 1 in seen:
                cur+=1
                count+=1
            result = max(result, count)
        
        return result