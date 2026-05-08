class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for i in range(n+1):
            xor^= i
        
        for num in nums:
            xor^=num
        return xor